# AddPipePenetration Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddPipePenetration`

Penetrates the adjacent fitting or pipe with the pipe that ends at the selected sketch point.
Penetrates the adjacent fitting or pipe with the pipe that ends at the selected sketch point.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddPipePenetration() As System.Integer
```

```

Dim instance As IAssemblyDoc
Dim value As System.Integer
 
value = instance.AddPipePenetration()
```

```

System.int AddPipePenetration()
```

```

System.int AddPipePenetration(); 
```

#### Return Value

Indicates the success or failure of the operation as defined in [swPipingPenetrationStatus\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPipingPenetrationStatus_e.html)

Remarks

If the routing DLL is not available, then COM returns ITF\_E\_ROUTINGNOTLOADED.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::AddPipingFitting Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddPipingFitting.md)
