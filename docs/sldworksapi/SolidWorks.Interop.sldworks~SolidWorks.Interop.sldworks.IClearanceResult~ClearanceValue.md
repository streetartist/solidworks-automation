# ClearanceValue Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceResult~ClearanceValue`

Gets the clearance value.
Gets the clearance value.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property ClearanceValue As System.Double
```

```

Dim instance As IClearanceResult
Dim value As System.Double
 
value = instance.ClearanceValue
```

```

System.double ClearanceValue {get;}
```

```

property System.double ClearanceValue {
   System.double get();
}
```

#### Property Value

Clearance value

Remarks

This property is valid only if [IClearanceResult::ClearanceType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceResult~ClearanceType.md) is [swClearanceType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swClearanceType_e.html).swClearanceType\_Distance.

Example

See the [IClearanceVerificationMgr](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IClearanceResult Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceResult.md)  
[IClearanceResult Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceResult_members.md)
