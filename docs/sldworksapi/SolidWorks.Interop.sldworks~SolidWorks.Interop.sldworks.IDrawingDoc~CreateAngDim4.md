# CreateAngDim4 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateAngDim4`

Creates a non-associative angular dimension.
Creates a non-associative angular dimension.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateAngDim4( _
   ByVal P0 As System.Object, _
   ByVal P1 As System.Object, _
   ByVal P2 As System.Object, _
   ByVal P3 As System.Object, _
   ByVal P4 As System.Object, _
   ByVal P5 As System.Object, _
   ByVal P6 As System.Object, _
   ByVal TextPoint As System.Object, _
   ByVal TextHeight As System.Double _
) As System.Object
```

```

Dim instance As IDrawingDoc
Dim P0 As System.Object
Dim P1 As System.Object
Dim P2 As System.Object
Dim P3 As System.Object
Dim P4 As System.Object
Dim P5 As System.Object
Dim P6 As System.Object
Dim TextPoint As System.Object
Dim TextHeight As System.Double
Dim value As System.Object
 
value = instance.CreateAngDim4(P0, P1, P2, P3, P4, P5, P6, TextPoint, TextHeight)
```

```

System.object CreateAngDim4( 
   System.object P0,
   System.object P1,
   System.object P2,
   System.object P3,
   System.object P4,
   System.object P5,
   System.object P6,
   System.object TextPoint,
   System.double TextHeight
)
```

```

System.Object^ CreateAngDim4( 
   System.Object^ P0,
   System.Object^ P1,
   System.Object^ P2,
   System.Object^ P3,
   System.Object^ P4,
   System.Object^ P5,
   System.Object^ P6,
   System.Object^ TextPoint,
   System.double TextHeight
) 
```

#### Parameters

*P0*
:   Array of 3 doubles (x,y,z); dimension end point

*P1*
:   Array of 3 doubles (x,y,z); dimension point

*P2*
:   Array of 3 doubles (x,y,z); extension1 start point

*P3*
:   Array of 3 doubles (x,y,z); extension1 end point

*P4*
:   Array of 3 doubles (x,y,z); extension2 start point

*P5*
:   Array of 3 doubles (x,y,z); extension2 end point

*P6*
:   Array of 3 doubles (x,y,z); plane normal

*TextPoint*
:   Array of 3 doubles (x,y,z); position of text

*TextHeight*
:   Text height in meters

#### Return Value

Newly created display dimension

Remarks

SOLIDWORKS creates this type of dimension between the two points that you specify. It has no relation to your geometry.

This method does not replace [IDrawingDoc::CreateDiamDim4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDiamDim4.md) or [IDrawingDoc::ICreateDiamDim4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateDiamDim4.md); it changes the number of arguments required to construct the [IDisplayDimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  object.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IDrawingDoc::ICreateAngDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateAngDim4.md)  
[IDrawingDoc::CreateLinearDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateLinearDim4.md)  
[IDrawingDoc::CreateOrdinateDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateOrdinateDim4.md)  
[IDrawingDoc::ICreateLinearDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateLinearDim4.md)  
[IDrawingDoc::ICreateOrdinateDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateOrdinateDim4.md)
