# SetPartnerKey Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwPEClassFactory~SetPartnerKey`

Sets the license key which SOLIDWORKS uses to verify SOLIDWORKS Partner entitlement.
Sets the license key which SOLIDWORKS uses to verify SOLIDWORKS Partner entitlement.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetPartnerKey( _
   ByVal StrPartnerEntitlement As System.String, _
   ByRef TokenObject As System.Object _
) As System.Integer
```

```

Dim instance As ISwPEClassFactory
Dim StrPartnerEntitlement As System.String
Dim TokenObject As System.Object
Dim value As System.Integer
 
value = instance.SetPartnerKey(StrPartnerEntitlement, TokenObject)
```

```

System.int SetPartnerKey( 
   System.string StrPartnerEntitlement,
   out System.object TokenObject
)
```

```

System.int SetPartnerKey( 
   System.String^ StrPartnerEntitlement,
   [Out] System.Object^ TokenObject
) 
```

#### Parameters

*StrPartnerEntitlement*
:   License key string (see **Remarks**)

*TokenObject*
:   [ISwPEToken](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwPEToken.md) (**for** **future use only - see Remarks**)

#### Return Value

Return code as defined by [swPartnerEntitlementStatus\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPartnerEntitlementStatus_e.html)

Remarks

When this method is called, SOLIDWORKS compares the registry against these values in the license key specified in StrPartnerEntitlement:

- SOLIDWORKS Partner entitlement
- SOLIDWORKS version
- Add-in name
- Add-in GUID
- Expiration date

See [SOLIDWORKS Partner Program](ms-its:sldworksapiprogguide.chm::/GettingStarted/SolidWorks_Partner_Program_2.htm).

TokenObject is for future use only.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISwPEClassFactory Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwPEClassFactory.md)  
[ISwPEClassFactory Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwPEClassFactory_members.md)
