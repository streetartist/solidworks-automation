# ICreateTempBodyFromSurfaces Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateTempBodyFromSurfaces`

Creates a temporary body from a list of existing trimmed surfaces.
Creates a temporary body from a list of existing trimmed surfaces.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateTempBodyFromSurfaces() As Body2
```

```

Dim instance As IBody2
Dim value As Body2
 
value = instance.ICreateTempBodyFromSurfaces()
```

```

Body2 ICreateTempBodyFromSurfaces()
```

```

Body2^ ICreateTempBodyFromSurfaces(); 
```

#### Return Value

Temporary [body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

Remarks

This method is the final call to a set of related functions (same as [IBody2::CreateBodyFromSurfaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateBodyFromSurfaces.md)) that are designed to construct a temporary body from trimmed surfaces.

The first call in this process should be to [IPartDoc::CreateNewBody2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ICreateNewBody2.md), so as to arrange for a placeholder for all the trimmed surfaces.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IBody2::CreateTempBodyFromSurfaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateTempBodyFromSurfaces.md)
