# AutoDimension Method (IDrawingDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AutoDimension`

Automatically dimensions the selected drawing view.
Automatically dimensions the selected drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AutoDimension( _
   ByVal EntitiesToDimension As System.Integer, _
   ByVal HorizontalScheme As System.Integer, _
   ByVal HorizontalPlacement As System.Integer, _
   ByVal VerticalScheme As System.Integer, _
   ByVal VerticalPlacement As System.Integer _
) As System.Integer
```

```

Dim instance As IDrawingDoc
Dim EntitiesToDimension As System.Integer
Dim HorizontalScheme As System.Integer
Dim HorizontalPlacement As System.Integer
Dim VerticalScheme As System.Integer
Dim VerticalPlacement As System.Integer
Dim value As System.Integer
 
value = instance.AutoDimension(EntitiesToDimension, HorizontalScheme, HorizontalPlacement, VerticalScheme, VerticalPlacement)
```

```

System.int AutoDimension( 
   System.int EntitiesToDimension,
   System.int HorizontalScheme,
   System.int HorizontalPlacement,
   System.int VerticalScheme,
   System.int VerticalPlacement
)
```

```

System.int AutoDimension( 
   System.int EntitiesToDimension,
   System.int HorizontalScheme,
   System.int HorizontalPlacement,
   System.int VerticalScheme,
   System.int VerticalPlacement
) 
```

#### Parameters

*EntitiesToDimension*
:   Entities to dimension as defined in [swAutodimEntities\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAutodimEntities_e.html)

*HorizontalScheme*
:   Horizontal dimensioning scheme as defined in [swAutodimScheme\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAutodimScheme_e.html)

*HorizontalPlacement*
:   Placement relative to the drawing view as defined in [swAutodimHorizontalPlacement\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAutodimHorizontalPlacement_e.html)

*VerticalScheme*
:   Vertical dimensioning scheme as defined in [swAutodimScheme\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAutodimScheme_e.html)

*VerticalPlacement*
:   Placement relative to the drawing view as defined in [swAutodimVerticalPlacement\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAutodimVerticalPlacement_e.html)

#### Return Value

swAutodimStatusSuccess if the view is automatically dimensioned; see [swAutodimStatus\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAutodimStatus_e.html) for reasons for possible failures

Remarks

This method requires information about the:

- drawing view to autodimension. This information can be supplied by selecting the drawing view to use. No mark is necessary.  
    
  If a drawing view is not selected, then this method attempts to determine the drawing view information from the other entities that are selected. If no other selections exist, then this method defaults to using the first drawing view, which is consistent with how the SOLIDWORKS user interface works.
- datums to use for the dimensioning baseline. These can be supplied by selecting a vertical edge, vertical sketch line, vertex, or sketch point as the datum for the horizontal dimensioning scheme. Mark the selection with swAutodimMarkHorizontalDatum from [swAutodimMark\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAutodimMark_e.html). Similarly a horizontal edge, horizontal sketch line, vertex, or sketch point should be selected and marked with swAutodimMark\_e.swAutodimMarkVerticalDatum for defining the datum for the vertical dimensioning scheme. If only one of these datums is supplied, only the appropriate dimensions are created for that datum.  
    
  Instead of selecting the horizontal and vertical datum separately, you can select a vertex or sketch point to use to define both datums. Mark the selected vertex or sketch point selection with swAutodimMark\_e.swAutodimMarkOriginDatum. If no datums are selected, then this method automatically uses the left- and bottom-most entities in the view to determine default datums, which is consistent with how the SOLIDWORKS user interface works.
- entities to autodimension. This information is supplied by the entitiesToDimension argument and the selected entities marked with swAutodimMark\_e.swAutodimMarkEntities. The entitiesToDimension argument takes a value from the swAutodimEntities\_e enumeration:

  - swAutodimEntitiesSelected indicates that only selected entities marked with a value of swAutodimMarkEntities are considered for autodimensioning.
  - swAutodimEntitiesAll indicates that all entities in the drawing view are autodimensioned.
  - swAutodimEntitiesBasedOnPreselect indicates that SOLIDWORKS figures out what to do based on the selected entities marked with swAutodimMarkEntities. If any exist, then autodimension them, just like swAutodimEntitiesSelected. If none exist, then autodimension all entities, just like swAutodimEntitiesAll.  
      
    Supported entities for dimensioning are lines, points, vertices, faces, and sketch entities.

Example

[Autodimension Selected Drawing View (C#)](Autodimension_Selected_Drawing_View_Example_CSharp.htm)  
[Autodimension Selected Drawing View (VB.NET)](Autodimension_Selected_Drawing_View_Example_VBNET.htm)  
[Autodimension Selected Drawing View (VBA)](Autodimension_Selected_Drawing_View_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IDrawingDoc:AddChamferDim Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AddChamferDim.md)  
[IDrawingDoc:CreateAngDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateAngDim4.md)  
[IDrawingDoc:CreateDiamDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDiamDim4.md)  
[IDrawingDoc:CreateLinearDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateLinearDim4.md)  
[IDrawingDoc:CreateOrdinateDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateOrdinateDim4.md)  
[IDrawingDoc:Dimensions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~Dimensions.md)  
[IDrawingDoc:DragModelDimension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~DragModelDimension.md)  
[IDrawingDoc:HideShowDimensions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~HideShowDimensions.md)  
[IDrawingDoc:IAddChamferDim Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IAddChamferDim.md)  
[IDrawingDoc:ICreateAngDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateAngDim4.md)  
[IDrawingDoc:ICreateDiamDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateDiamDim4.md)  
[IDrawingDoc:ICreateLinearDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateLinearDim4.md)  
[IDrawingDoc:ICreateOrdinateDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateOrdinateDim4.md)  
[IDrawingDoc:InsertBaseDim Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertBaseDim.md)  
[IDrawingDoc:InsertHorizontalOrdinate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertHorizontalOrdinate.md)  
[IDrawingDoc:InsertModelAnnotations3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertModelAnnotations3.md)  
[IDrawingDoc:InsertModelDimensions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertModelDimensions.md)  
[IDrawingDoc:InsertOrdinate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertOrdinate.md)  
[IDrawingDoc:InsertRefDim Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertRefDim.md)  
[IDrawingDoc:InsertVerticalOrdinate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertVerticalOrdinate.md)  
[IDrawingDoc::SketchDim Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SketchDim.md)  
[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)
