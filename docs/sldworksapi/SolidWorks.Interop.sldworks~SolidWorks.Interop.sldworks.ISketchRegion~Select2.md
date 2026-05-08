# Select2 Method (ISketchRegion)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRegion~Select2`

Selects the sketch region and marks it.
Selects the sketch region and marks it.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Select2( _
   ByVal Append As System.Boolean, _
   ByVal Data As SelectData _
) As System.Boolean
```

```

Dim instance As ISketchRegion
Dim Append As System.Boolean
Dim Data As SelectData
Dim value As System.Boolean
 
value = instance.Select2(Append, Data)
```

```

System.bool Select2( 
   System.bool Append,
   SelectData Data
)
```

```

System.bool Select2( 
   System.bool Append,
   SelectData^ Data
) 
```

#### Parameters

*Append*
:   True to append this selection to the selection list, false to replace the selection list with this selection

*Data*
:   [ISelectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData.md) object

#### Return Value

True if the sketch region is selected, false if not

Example

[Get Sketch Regions (VBA)](Get_Sketch_Regions_Example_VB.htm)  
[Get Sketch Regions (VB.NET)](Get_Sketch_Regions_Example_VBNET.htm)  
[Get Sketch Regions (C#)](Get_Sketch_Regions_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchRegion Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRegion.md)  
[ISketchRegion Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRegion_members.md)  
[ISketchRegion::DeSelect Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRegion~DeSelect.md)
