# IgnoreClearanceEqualToSpecifiedValue Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr~IgnoreClearanceEqualToSpecifiedValue`

Gets or sets whether to ignore clearances equal to or greater than IClearanceVerificationMgr::GetMinimumAcceptableClearance.
Gets or sets whether to ignore clearances equal to or greater than [IClearanceVerificationMgr::GetMinimumAcceptableClearance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr~GetMinimumAcceptableClearance.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property IgnoreClearanceEqualToSpecifiedValue As System.Boolean
```

```

Dim instance As IClearanceVerificationMgr
Dim value As System.Boolean
 
instance.IgnoreClearanceEqualToSpecifiedValue = value
 
value = instance.IgnoreClearanceEqualToSpecifiedValue
```

```

System.bool IgnoreClearanceEqualToSpecifiedValue {get; set;}
```

```

property System.bool IgnoreClearanceEqualToSpecifiedValue {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to ignore clearances equal to or greater than the specified value, false to not

Remarks

If this property is true, use [IClearanceVerificationMgr::SetMinimumAcceptableClearance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr~SetMinimumAcceptableClearance.md) to specify the minimum clearance value, at or above which clearances are ignored.

Example

See the [IClearanceVerificationMgr](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IClearanceVerificationMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr.md)  
[IClearanceVerificationMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr_members.md)
