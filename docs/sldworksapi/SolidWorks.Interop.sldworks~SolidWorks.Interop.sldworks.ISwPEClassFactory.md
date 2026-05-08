# ISwPEClassFactory Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwPEClassFactory`

Allows access to the callback object used by ISwPEManager to send a license key back to SOLIDWORKS for SOLIDWORKS Partner entitlement verification.
Allows access to the callback object used by [ISwPEManager](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwPEManager.md) to send a license key back to SOLIDWORKS for SOLIDWORKS Partner entitlement verification.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface ISwPEClassFactory 
```

```

Dim instance As ISwPEClassFactory
```

```

public interface ISwPEClassFactory 
```

```

public interface class ISwPEClassFactory 
```

Remarks

This interface provides a callback mechanism in which:

1. SOLIDWORKS requests the partner's key through the add-in by calling [ISwPEManager::IdentifyToSW](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwPEManager~IdentifyToSW.md),
2. The partner add-in sends a license key back to SOLIDWORKS in [ISwPEClassFactory::SetPartnerKey](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwPEClassFactory~SetPartnerKey.md), and
3. SOLIDWORKS uses the license key to verify the entitlement of the SOLIDWORKS Partner and returns [ISwPEToken](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwPEToken.md).

 See [SOLIDWORKS Partner Program](ms-its:sldworksapiprogguide.chm::/GettingStarted/SolidWorks_Partner_Program_2.htm).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISwPEClassFactory Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwPEClassFactory_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
