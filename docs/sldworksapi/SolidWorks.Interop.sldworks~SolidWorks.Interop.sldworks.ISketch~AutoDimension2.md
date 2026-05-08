# AutoDimension2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~AutoDimension2`

Obsolete. Superseded by ISketchManager::FullyDefineSketch.
Obsolete. Superseded by [ISketchManager::FullyDefineSketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~FullyDefineSketch.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AutoDimension2( _
   ByVal EntitiesToDimension As System.Integer, _
   ByVal HorizontalScheme As System.Integer, _
   ByVal HorizontalPlacement As System.Integer, _
   ByVal VerticalScheme As System.Integer, _
   ByVal VerticalPlacement As System.Integer _
) As System.Integer
```

```

Dim instance As ISketch
Dim EntitiesToDimension As System.Integer
Dim HorizontalScheme As System.Integer
Dim HorizontalPlacement As System.Integer
Dim VerticalScheme As System.Integer
Dim VerticalPlacement As System.Integer
Dim value As System.Integer
 
value = instance.AutoDimension2(EntitiesToDimension, HorizontalScheme, HorizontalPlacement, VerticalScheme, VerticalPlacement)
```

```

System.int AutoDimension2( 
   System.int EntitiesToDimension,
   System.int HorizontalScheme,
   System.int HorizontalPlacement,
   System.int VerticalScheme,
   System.int VerticalPlacement
)
```

```

System.int AutoDimension2( 
   System.int EntitiesToDimension,
   System.int HorizontalScheme,
   System.int HorizontalPlacement,
   System.int VerticalScheme,
   System.int VerticalPlacement
) 
```

#### Parameters

*EntitiesToDimension*
:   Entities to dimension as defined in [swAutodimEntities\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAutodimEntities_e.html)

*HorizontalScheme*
:   Horizontal dimensioning scheme as defined in [swAutodimScheme\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAutodimScheme_e.html)

*HorizontalPlacement*
:   Placement relative to the sketch as defined in [swAutodimHorizontalPlacement\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAutodimHorizontalPlacement_e.html)

*VerticalScheme*
:   Vertical dimensioning scheme as defined in [swAutodimScheme\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAutodimScheme_e.html)

*VerticalPlacement*
:   Placement relative to the sketch as defined in [swAutodimVerticalPlacement\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAutodimVerticalPlacement_e.html)

#### Return Value

swAutodimStatusSuccess if the sketch is automatically dimensioned successfully; see [swAutodimStatus\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAutodimStatus_e.html) for values for reasons for possible failures

Remarks

If the EntitiesToDimension argument takes the value swAutodimEntitiesSelected, then use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) with a mark value of swAutodimMarkEntities to select the sketch entities to dimension.

You can supply datums for horizontal and vertical dimensioning schemes. Select and mark a unique vertical edge, vertex, sketch point, or vertical sketch line as the datum for the horizontal dimensioning scheme, using swAutodimMarkHorizontalDatum as the mark value. Similarly, select a unique horizontal edge, vertex, sketch point, or horizontal sketch line as the datum for the vertical dimensioning scheme, using swAutodimMarkVerticalDatum as the mark value. It is an error to supply just one datum as indicated by the status value swAutodimStatus\_DatumNotSupplied.

Example

[Autodimension a Sketch (VBA)](Autodimension_a_Sketch_Example_VB.htm)  
[Insert DXF File and Add Dimension (VBA)](Insert_DXF_File_and_Add_Dimension_Example_VB.htm)  
[Autodimension All Sketches (C#)](Autodimension_All_Sketches_Example_CSharp.htm)  
[Autodimension All Sketches (VB.NET)](Autodimension_All_Sketches_Example_VBNET.htm)  
[Autodimension all Sketches (VBA)](Autodimension_All_Sketches_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)  
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.md)
