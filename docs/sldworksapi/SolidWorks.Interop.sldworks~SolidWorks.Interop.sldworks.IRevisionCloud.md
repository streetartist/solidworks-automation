# IRevisionCloud Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud`

Allows access to a revision cloud annotation.
Allows access to a revision cloud annotation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IRevisionCloud 
```

```

Dim instance As IRevisionCloud
```

```

public interface IRevisionCloud 
```

```

public interface class IRevisionCloud 
```

Remarks

To create a revision cloud in a drawing document, call:

1. [IDrawingDoc::InsertRevisionCloud](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertRevisionCloud.md) or [IDrawingDoc::IInsertRevisionCloud](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IInsertRevisionCloud.md).
2. [IRevisionCloud::GetAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud~GetAnnotation.md) or [IRevisionCloud::IGetAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud~IGetAnnotation.md) to get the annotation object for the revision cloud.
3. [IAnnotation::SetPosition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetPosition.md) to set the revision cloud position point on the drawing. If you eliminate this step, the revision cloud is rendered starting at the drawing origin of x=0, y=0, z=0. Set the revision cloud position point as follows:

   | For revision cloud shape... | Set the revision cloud position point to... |
   | --- | --- |
   | Ellipse | The center of the revision cloud. |
   | Rectangle | A corner of the revision cloud. |
   | Polygon | One of the points on the revision cloud. |
   | Freehand | One of the points on the revision cloud. |
4. [IRevisionCloud::ArcRadius](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud~ArcRadius.md) to set the arc radius of the revision cloud.
5. [IRevisionCloud::SetPathPointAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud~SetPathPointAtIndex.md) one or more times with Index = -1 to create points on the revision cloud as follows:

   | For revision cloud shape... | Call IRevisionCloud::SetPathPointAtIndex... |
   | --- | --- |
   | Ellipse | Once, specifying the coordinates of a corner of the ellipse-inscribed rectangle. |
   | Rectangle | Once, specifying the coordinates of a corner opposite the revision cloud position point. |
   | Polygon | (Number of polygon sides + 1) times, such that the first and last points coincide with the revision cloud position point. |
   | Freehand | Indefinite number of times, such that the first and last points coincide with the revision cloud position point. |
6. [IRevisionCloud::Finalize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud~Finalize.md) to close the revision cloud path. Once the revision cloud path is closed, you can no longer add points to it.
7. IRevisionCloud::SetPathPointAtIndex to modify the position of an existing point on the revision cloud.

Example

[Insert Revision Cloud into a Drawing (VBA)](Insert_Revision_Cloud_into_Drawing_Example_VB.htm)  
[Insert Revision Cloud into a Drawing (VB.NET)](Insert_Revision_Cloud_into_Drawing_Example_VBNET.htm)  
[Insert Revision Cloud into a Drawing (C#)](Insert_Revision_Cloud_into_Drawing_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRevisionCloud Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
