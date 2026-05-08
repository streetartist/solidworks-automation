# ClearanceType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceResult~ClearanceType`

Gets the clearance type.
Gets the clearance type.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property ClearanceType As System.Integer
```

```

Dim instance As IClearanceResult
Dim value As System.Integer
 
value = instance.ClearanceType
```

```

System.int ClearanceType {get;}
```

```

property System.int ClearanceType {
   System.int get();
}
```

#### Property Value

Clearance type as defined by [swClearanceType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swClearanceType_e.html)

Example

See the [IClearanceVerificationMgr](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IClearanceResult Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceResult.md)  
[IClearanceResult Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceResult_members.md)
