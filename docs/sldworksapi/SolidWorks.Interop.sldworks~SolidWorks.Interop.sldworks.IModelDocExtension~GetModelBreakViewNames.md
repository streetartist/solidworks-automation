# GetModelBreakViewNames Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetModelBreakViewNames`

Gets the names and number of the Model Break Views in the current configuration of the active model.
Gets the names and number of the Model Break Views in the current configuration of the active model.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetModelBreakViewNames( _
   ByRef Views As System.Object _
) As System.Integer
```

```

Dim instance As IModelDocExtension
Dim Views As System.Object
Dim value As System.Integer
 
value = instance.GetModelBreakViewNames(Views)
```

```

System.int GetModelBreakViewNames( 
   out System.object Views
)
```

```

System.int GetModelBreakViewNames( 
   [Out] System.Object^ Views
) 
```

#### Parameters

*Views*
:   Names of Model Break Views

#### Return Value

Number of Model Break Views

Example

[Get Names and Show Model Break Views (C#)](Get_Names_and_Show_Model_Break_Views_Example_CSharp.htm)  
[Get Names and Show Model Break Views (VB.NET)](Get_Names_and_Show_Model_Break_Views_Example_VBNET.htm)  
[Get Names and Show Model Break Views (VBA)](Get_Names_and_Show_Model_Break_Views_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::ShowModelBreakView Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ShowModelBreakView.md)  
[IView3D::ModelBreakViewName Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D~ModelBreakViewName.md)
