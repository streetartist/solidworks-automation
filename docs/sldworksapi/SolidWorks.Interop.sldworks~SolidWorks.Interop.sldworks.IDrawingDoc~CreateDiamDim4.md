# CreateDiamDim4 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDiamDim4`

Creates a non-associative diameter dimension.
Creates a non-associative diameter dimension.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateDiamDim4( _
   ByVal P0 As System.Object, _
   ByVal P1 As System.Object, _
   ByVal P2 As System.Object, _
   ByVal P3 As System.Object, _
   ByVal TextPoint As System.Object, _
   ByVal Val As System.Double, _
   ByVal TextHeight As System.Double _
) As System.Object
```

```

Dim instance As IDrawingDoc
Dim P0 As System.Object
Dim P1 As System.Object
Dim P2 As System.Object
Dim P3 As System.Object
Dim TextPoint As System.Object
Dim Val As System.Double
Dim TextHeight As System.Double
Dim value As System.Object
 
value = instance.CreateDiamDim4(P0, P1, P2, P3, TextPoint, Val, TextHeight)
```

```

System.object CreateDiamDim4( 
   System.object P0,
   System.object P1,
   System.object P2,
   System.object P3,
   System.object TextPoint,
   System.double Val,
   System.double TextHeight
)
```

```

System.Object^ CreateDiamDim4( 
   System.Object^ P0,
   System.Object^ P1,
   System.Object^ P2,
   System.Object^ P3,
   System.Object^ TextPoint,
   System.double Val,
   System.double TextHeight
) 
```

#### Parameters

*P0*
:   Array of 3 doubles (x,y,z); location of dimension point

*P1*
:   Array of 3 doubles (x,y,z); nearest point on circle

*P2*
:   Array of 3 doubles (x,y,z); farthest point on circle diametrically opposite to P1

*P3*
:   Array of 3 doubles (x,y,z); plane normal

*TextPoint*
:   Array of 3 doubles (x,y,z); position of text

*Val*
:   Dimension value in meters

*TextHeight*
:   Text height in meters

#### Return Value

Newly created display dimension

Remarks

SOLIDWORKS creates this type of dimension between the two points you specify. It has no relation to your geometry.

Example

[Create Non-associative Diameter Dimension (VBA)](Create_Non-associative_Diameter_Dimension_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IDrawingDoc::ICreateDiamDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateDiamDim4.md)  
[IDrawingDoc::IICreateAngDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateAngDim4.md)  
[IDrawingDoc::ICreateAngDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateAngDim4.md)  
[IDrawingDoc::ICreateLinearDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateLinearDim4.md)  
[IDrawingDoc::IICreateLinearDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateLinearDim4.md)  
[IDrawingDoc::IICreateOrdinateDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateOrdinateDim4.md)  
[IDrawingDoc::ICreateOrdinateDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateOrdinateDim4.md)
