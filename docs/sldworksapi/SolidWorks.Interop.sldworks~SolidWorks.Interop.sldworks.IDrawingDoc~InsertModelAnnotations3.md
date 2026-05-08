# InsertModelAnnotations3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertModelAnnotations3`

Inserts model annotations into this drawing document's currently selected drawing view.
Inserts model annotations into this drawing document's currently selected drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertModelAnnotations3( _
   ByVal Option As System.Integer, _
   ByVal Types As System.Integer, _
   ByVal AllViews As System.Boolean, _
   ByVal DuplicateDims As System.Boolean, _
   ByVal HiddenFeatureDims As System.Boolean, _
   ByVal UsePlacementInSketch As System.Boolean _
) As System.Object
```

```

Dim instance As IDrawingDoc
Dim Option As System.Integer
Dim Types As System.Integer
Dim AllViews As System.Boolean
Dim DuplicateDims As System.Boolean
Dim HiddenFeatureDims As System.Boolean
Dim UsePlacementInSketch As System.Boolean
Dim value As System.Object
 
value = instance.InsertModelAnnotations3(Option, Types, AllViews, DuplicateDims, HiddenFeatureDims, UsePlacementInSketch)
```

```

System.object InsertModelAnnotations3( 
   System.int Option,
   System.int Types,
   System.bool AllViews,
   System.bool DuplicateDims,
   System.bool HiddenFeatureDims,
   System.bool UsePlacementInSketch
)
```

```

System.Object^ InsertModelAnnotations3( 
   System.int Option,
   System.int Types,
   System.bool AllViews,
   System.bool DuplicateDims,
   System.bool HiddenFeatureDims,
   System.bool UsePlacementInSketch
) 
```

#### Parameters

*Option*
:   Source of dimensions as defined by [swImportModelItemsSource\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swImportModelItemsSource_e.html) (see Remarks)

*Types*
:   Bitwise OR of annotation types as defined in [swInsertAnnotation\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInsertAnnotation_e.html)

*AllViews*
:   True to insert the annotations in all views in the drawing, false to insert annotations only in the selected view

*DuplicateDims*
:   True to eliminate duplicate dimensions, false to allow duplicate dimensions

*HiddenFeatureDims*
:   True to insert dimensions from features that are hidden, false to not insert dimensions from features that are hidden

*UsePlacementInSketch*
:   True to insert dimensions as they were placed in sketch, false to not

#### Return Value

Array of inserted [IAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md) objects

Remarks

The Option argument was incorrectly documented in versions of the SOLIDWORKS API Help published before SOLIDWORKS 2008 SP3.

|  |  |
| --- | --- |
| Incorrect | Correct |
| 0 - All dimensions in the view | swImportModelItemsFromEntireModel = 0 |
| 1 - All dimensions of the currently selected component (for assembly drawings) | swImportModelItemsFromSelectedFeature = 1 |
| 2 - All dimensions of the currently selected feature | swImportModelItemsFromSelectedComponent = 2 |
| All dimensions of the assembly | - swImportModelItemsFromAssemblyOnly = 3 |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IDrawingDoc::AddCenterMark Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AddCenterMark.md)  
[IDrawingDoc::AddChamferDim Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AddChamferDim.md)  
[IDrawingDoc::AddHoleCallout2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AddHoleCallout2.md)  
[IDrawingDoc::Dimensions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~Dimensions.md)  
[IDrawingDoc::INewGtol Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~INewGtol.md)  
[IDrawingDoc::InsertBaseDim Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertBaseDim.md)  
[IDrawingDoc::ICreateText2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateText2.md)  
[IDrawingDoc::CreateText2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateText2.md)  
[IDrawingDoc::CreateCompoundNote Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateCompoundNote.md)  
[IDrawingDoc::IAddHoleCallout2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IAddHoleCallout2.md)  
[IDrawingDoc::ICreateCompoundNote Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateCompoundNote.md)  
[IDrawingDoc::InsertDatumTag Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertDatumTag.md)  
[IDrawingDoc::InsertNewNote2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertNewNote2.md)  
[IDrawingDoc::InsertRefDim Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertRefDim.md)  
[IDrawingDoc::InsertRevisionSymbol Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertRevisionSymbol.md)  
[IDrawingDoc::InsertSurfaceFinishSymbol Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertSurfaceFinishSymbol.md)  
[IDrawingDoc::InsertThreadCallout Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertThreadCallout.md)  
[IDrawingDoc::InsertWeldSymbol Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertWeldSymbol.md)  
[IDrawingDoc::NewGtol Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~NewGtol.md)  
[IDrawingDoc::NewNote Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~NewNote.md)  
[IDrawingDoc::AttachAnnotation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AttachAnnotation.md)
