# CreateFlatPatternViewFromModelView2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateFlatPatternViewFromModelView2`

Obsolete. Superseded by IDrawingDoc::CreateFlatPatternViewFromModelView3.
Obsolete. Superseded by [IDrawingDoc::CreateFlatPatternViewFromModelView3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateFlatPatternViewFromModelView3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateFlatPatternViewFromModelView2( _
   ByVal ModelName As System.String, _
   ByVal ConfigName As System.String, _
   ByVal LocX As System.Double, _
   ByVal LocY As System.Double, _
   ByVal LocZ As System.Double, _
   ByVal HideBendLines As System.Boolean _
) As System.Boolean
```

```

Dim instance As IDrawingDoc
Dim ModelName As System.String
Dim ConfigName As System.String
Dim LocX As System.Double
Dim LocY As System.Double
Dim LocZ As System.Double
Dim HideBendLines As System.Boolean
Dim value As System.Boolean
 
value = instance.CreateFlatPatternViewFromModelView2(ModelName, ConfigName, LocX, LocY, LocZ, HideBendLines)
```

```

System.bool CreateFlatPatternViewFromModelView2( 
   System.string ModelName,
   System.string ConfigName,
   System.double LocX,
   System.double LocY,
   System.double LocZ,
   System.bool HideBendLines
)
```

```

System.bool CreateFlatPatternViewFromModelView2( 
   System.String^ ModelName,
   System.String^ ConfigName,
   System.double LocX,
   System.double LocY,
   System.double LocZ,
   System.bool HideBendLines
) 
```

#### Parameters

*ModelName*
:   Name of model

*ConfigName*
:   Name of configuration

*LocX*
:   X coordinate

*LocY*
:   Y coordinate

*LocZ*
:   Z coordinate

*HideBendLines*
:   True hides bend lines, false does not

#### Return Value

True if the flat-pattern view was created successfully, false if it was not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IDrawingDoc::ChangeRefConfigurationOfFlatPatternView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ChangeRefConfigurationOfFlatPatternView.md)  
[IDrawingDoc::CreateDrawViewFromModelView3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDrawViewFromModelView3.md)
