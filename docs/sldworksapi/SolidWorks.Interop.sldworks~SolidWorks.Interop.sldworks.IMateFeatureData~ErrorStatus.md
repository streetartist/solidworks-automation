# ErrorStatus Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateFeatureData~ErrorStatus`

Gets the status of adding or editing this mate.
Gets the status of adding or editing this mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property ErrorStatus As System.Integer
```

```

Dim instance As IMateFeatureData
Dim value As System.Integer
 
value = instance.ErrorStatus
```

```

System.int ErrorStatus {get;}
```

```

property System.int ErrorStatus {
   System.int get();
}
```

#### Property Value

Status of adding or editing this mate as defined in [swAddMateError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAddMateError_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateFeatureData.md)  
[IMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateFeatureData_members.md)
