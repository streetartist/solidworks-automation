# ModelBreakViewName Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D~ModelBreakViewName`

Gets the name of the Model Break View in this 3D View.
Gets the name of the Model Break View in this 3D View.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property ModelBreakViewName As System.String
```

```

Dim instance As IView3D
Dim value As System.String
 
value = instance.ModelBreakViewName
```

```

System.string ModelBreakViewName {get;}
```

```

property System.String^ ModelBreakViewName {
   System.String^ get();
}
```

#### Property Value

Name of the Model Break View in this 3D View

Example

[Capture 3D View (C#)](Capture_3DView_Example_CSharp.htm)  
[Capture 3D View (VB.NET)](Capture_3DView_Example_VBNET.htm)  
[Capture 3D View (VBA)](Capture_3DView_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView3D Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D.md)  
[IView3D Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D_members.md)  
[IModelDocExtension::GetModelBreakViewNames Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetModelBreakViewNames.md)
