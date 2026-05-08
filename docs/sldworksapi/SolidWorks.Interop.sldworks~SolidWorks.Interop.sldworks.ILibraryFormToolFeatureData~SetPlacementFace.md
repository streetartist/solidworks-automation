# SetPlacementFace Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData~SetPlacementFace`

Specifies the face and pickpoint where the forming tool is inserted.
Specifies the face and pickpoint where the forming tool is inserted.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetPlacementFace( _
   ByVal Face As System.Object, _
   ByVal PickPoint As System.Object _
) 
```

```

Dim instance As ILibraryFormToolFeatureData
Dim Face As System.Object
Dim PickPoint As System.Object
 
instance.SetPlacementFace(Face, PickPoint)
```

```

void SetPlacementFace( 
   System.object Face,
   System.object PickPoint
)
```

```

void SetPlacementFace( 
   System.Object^ Face,
   System.Object^ PickPoint
) 
```

#### Parameters

*Face*
:   [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)

*PickPoint*
:   [IMathPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md)

Example

See the [ILibraryFormToolFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILibraryFormToolFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData.md)  
[ILibraryFormToolFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData_members.md)  
[ILibraryFormToolFeatureData::PlacementFace Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData~PlacementFace.md)
