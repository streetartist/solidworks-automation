# IInsertRevisionCloud Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IInsertRevisionCloud`

Inserts a revision cloud annotation with the specified shape into a view or sheet.
Inserts a revision cloud annotation with the specified shape into a view or sheet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IInsertRevisionCloud( _
   ByVal CloudShape As System.Integer _
) As RevisionCloud
```

```

Dim instance As IDrawingDoc
Dim CloudShape As System.Integer
Dim value As RevisionCloud
 
value = instance.IInsertRevisionCloud(CloudShape)
```

```

RevisionCloud IInsertRevisionCloud( 
   System.int CloudShape
)
```

```

RevisionCloud^ IInsertRevisionCloud( 
   System.int CloudShape
) 
```

#### Parameters

*CloudShape*
:   Revision cloud annotation shape as defined in [swRevisionCloudShape\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRevisionCloudShape_e.html)

#### Return Value

- in-process, unmanaged C++: Pointer to an [IRevisionCloud](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud.md)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

After calling this method:

1. Call [IRevisionCloud::IGetAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud~IGetAnnotation.md) to get the annotation object for the revision cloud.
2. Call [IAnnotation::SetPosition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetPosition.md) to set the revision cloud position point on the drawing. If you eliminate this step, the revision cloud is rendered starting at the drawing origin of x=0, y=0, z=0. Set the revision cloud position point as follows:

   | For revision cloud shape... | Set the revision cloud position point to... |
   | --- | --- |
   | Ellipse | The center of the revision cloud. |
   | Rectangle | A corner of the revision cloud. |
   | Polygon | One of the points on the revision cloud. |
   | Freehand | One of the points on the revision cloud. |
3. Call [IRevisionCloud::ArcRadius](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud~ArcRadius.md) to set the arc radius of the revision cloud.
4. Call [IRevisionCloud::SetPathPointAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud~SetPathPointAtIndex.md) with Index = -1 to create points on the revision cloud as follows:

   | For revision cloud shape... | Call IRevisionCloud::SetPathPointAtIndex... |
   | --- | --- |
   | Ellipse | Once, specifying the coordinates of a corner of the ellipse-inscribed rectangle. |
   | Rectangle | Once, specifying the coordinates of a corner opposite the revision cloud position point. |
   | Polygon | (Number of polygon sides + 1) times, such that the first and last points coincide with the revision cloud position point. |
   | Freehand | Indefinite number of times, such that the first and last points coincide with the revision cloud position point. |
5. Call [IRevisionCloud::Finalize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud~Finalize.md) to close the revision cloud path. Once the revision cloud path is closed, you can no longer add points to it.
6. Call IRevisionCloud::SetPathPointAtIndex to modify the position of an existing point on the revision cloud.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IView::InsertRevisionCloud Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertRevisionCloud.md)
