// Design Locker Type
public enum LockerType
{
	X-Small = 0,
	Small = 1,
	Medium = 2,
	Large = 3,
	X-Large = 4,
}

// Design Locker Class
public class Locker
{
	public Guid lockerId;
	public LockerType type;
	public int LocalId;
	public Locker(Guid id, LockerType type)
	{
		lockerId = id;
		this.type = type;
	}
	public Locker(Guid id, LockerType type, int localId)
	{
		this.lockerId = id;
		this.type = type;
		this.localId = localId;
	}
}

// Design Locker Manager
public class LockerManager
{
	private Guid lockerManagerId;
	private Dictionary<Locker, Guid?> lockers;
	public Address lockerAddress;
	private static LockerManager manager;
	private LockerManager(Guid managerId)
	{
		lockerManagerId = managerId;
		lockers = GetLockersByManager(managerId);
		lockerAddress = GetLockerManagerAddress(managerId);
	}
	
	public LockerManager GetInstance(Guid managerId)
	{
		if(manager == null)
		{
			manager = new LockerManager(managerId);
		}
		if(managerId != lockerManagerId)
		{
			throw new InvalidArgumentException("Invalid value Exception");
		}
		return manager;
	}
	
	public List<Locker> GetEmptyLockers()
	{
		return lockers.Where(x => x.Value == null).Select(x => x.Key).ToList<Locker>();
	}
	
	public Locker GetSingleEmptyLockerBytype(LockerType type)
	{
		return lockers.Where(x => (x.Value == null && x.Key.type = type)).Select(x => x.Key).FirstOrDefault();
	}
	
	public bool EmptyLocker(Guid lockerId)
	{
		var locker = lockers.Where(x => x.Key.lockerId == lockerId).Select(x => x.Key).FirstOrDefault();
		if(locker != null)
		{
			lockers[locker] = null;
			return true;
		}
		return false;
	}
	
	public bool EmptyLocker(Locker locker)
	{
		if(locker != null && lockers.ContainsKey(locker))
		{
			lockers[locker] = null;
			return true;
		}
		return false;
	}
	
	public bool EmptyLockerByProduct(Guid productCatalogId)
	{
		var locker = lockers.Where(x => x.Value == productCatalogId).Select(x => x.Key).FirstOrDefault();
		if(locker != null)
		{
			lockers[locker] = null;
			return true;
		}
		return false;
	}
	
	public bool FillLocker(Locker locker, Guid productCatalogId)
	{
		if(locker != null && lockers.ContainsKey(locker) && lockers[locker] == null)
		{
			lockers[locker] = productCatalogId;
			return true;
		}
		return false;
	}
	
	private Dictionary<Locker, bool> GetLockersByManager(Guid managerId)
	{
		var lockers = new Dictionary<Locker, bool>();
		var rowSets = GetLockersDetails(managerId);
		foreach(Row row in rowSets)
		{
			lockers.Add(
				new Locker(Guid.Parse(row[0]), Enum.Parse(row[1], typeof(LockerType)), Boolean.Parse(row[2]), Int32.PArse(row[3]))
				, Guid.Parse(row[4])); 
		}
		return lockers;
	}
}

// Amazon Locker class
public class AmazonLocker
{
	// User Requests
	public List<LockerManager> ShowMeLockers(Address userAddress)
	{
		// we use the address to list down top 10 nearest locker managers to the users. We can use Trie to implement this. Can use ZipCode or general address to navigate in the Trie.
		// once a user selects Locker Manager, we get locker Manager Id.
		// We initialize this locker Manager with Id or can use this Id to comminute with the locker manager.
	}
	
	lockerManager = LockerManager.GetInstance(managerId);
	var locker = lockerManager.GetSingleEmptyLockerBytype(LockerType.Medium); // type will be provided by the user, or Amazon can also determine type by the product calalog.
	lockerManager.FillLocker(locker, productCatalogId) // productCatalogId will be provided by the user.
	
	
	// when amazon guy comes in and remove the item, they call, EmptyLocker(Locker locker) from the locker manager itself to empty that locker.
	
}