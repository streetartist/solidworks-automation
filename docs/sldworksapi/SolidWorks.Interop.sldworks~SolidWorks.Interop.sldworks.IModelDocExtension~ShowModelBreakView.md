# ShowModelBreakView Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ShowModelBreakView`

Gets whether to show or hide the specified Model Break View in the current configuration of the active model.
Gets whether to show or hide the specified Model Break View in the current configuration of the active model.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ShowModelBreakView( _
   ByVal ShowView As System.Boolean, _
   ByVal ViewName As System.String _
) As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim ShowView As System.Boolean
Dim ViewName As System.String
Dim value As System.Boolean
 
value = instance.ShowModelBreakView(ShowView, ViewName)
```

```

System.bool ShowModelBreakView( 
   System.bool ShowView,
   System.string ViewName
)
```

```

System.bool ShowModelBreakView( 
   System.bool ShowView,
   System.String^ ViewName
) 
```

#### Parameters

*ShowView*
:   True to show the Model Break View, false to hide it

*ViewName*
:   Name of Model Break View to show or hide

#### Return Value

True if the method executed, false if it did not

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
[IModelDocExtension::GetModelBreakViewNames Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetModelBreakViewNames.md)
