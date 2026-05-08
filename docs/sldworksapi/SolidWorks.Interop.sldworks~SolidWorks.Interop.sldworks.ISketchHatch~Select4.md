# Select4 Method (ISketchHatch)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch~Select4`

Selects the sketch hatch and marks it.
Selects the sketch hatch and marks it.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Select4( _
   ByVal Append As System.Boolean, _
   ByVal Data As SelectData _
) As System.Boolean
```

```

Dim instance As ISketchHatch
Dim Append As System.Boolean
Dim Data As SelectData
Dim value As System.Boolean
 
value = instance.Select4(Append, Data)
```

```

System.bool Select4( 
   System.bool Append,
   SelectData Data
)
```

```

System.bool Select4( 
   System.bool Append,
   SelectData^ Data
) 
```

#### Parameters

*Append*
:   True appends the selection to the selection list, false replaces the selection list with this selection

*Data*
:   [ISelectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData.md) object

#### Return Value

True if the sketch hatch is selected, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchHatch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch.md)  
[ISketchHatch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch_members.md)  
[ISketchHatch::DeSelect Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch~DeSelect.md)
