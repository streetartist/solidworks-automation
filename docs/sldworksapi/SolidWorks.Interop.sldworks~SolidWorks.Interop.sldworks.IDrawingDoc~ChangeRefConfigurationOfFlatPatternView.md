# ChangeRefConfigurationOfFlatPatternView Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ChangeRefConfigurationOfFlatPatternView`

Changes the configuration of the selected flat-pattern view of the specified model.
Changes the configuration of the selected flat-pattern view of the specified model.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ChangeRefConfigurationOfFlatPatternView( _
   ByVal ModelName As System.String, _
   ByVal ConfigName As System.String _
) As System.Boolean
```

```

Dim instance As IDrawingDoc
Dim ModelName As System.String
Dim ConfigName As System.String
Dim value As System.Boolean
 
value = instance.ChangeRefConfigurationOfFlatPatternView(ModelName, ConfigName)
```

```

System.bool ChangeRefConfigurationOfFlatPatternView( 
   System.string ModelName,
   System.string ConfigName
)
```

```

System.bool ChangeRefConfigurationOfFlatPatternView( 
   System.String^ ModelName,
   System.String^ ConfigName
) 
```

#### Parameters

*ModelName*
:   Name of the model in the flat-pattern view

*ConfigName*
:   Name of the configuration

#### Return Value

True if the configuration was successfully changed, false if not

Remarks

Before calling this method, you must select the flat-pattern view of the model.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[DrawingDoc::CreateFlatPatternViewFromModelView2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateFlatPatternViewFromModelView2.md)
