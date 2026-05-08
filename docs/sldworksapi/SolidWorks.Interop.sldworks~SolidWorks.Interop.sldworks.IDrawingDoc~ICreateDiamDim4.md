# ICreateDiamDim4 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateDiamDim4`

Creates a non-associative diameter dimension.
Creates a non-associative diameter dimension.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateDiamDim4( _
   ByRef P0 As System.Double, _
   ByRef P1 As System.Double, _
   ByRef P2 As System.Double, _
   ByRef P3 As System.Double, _
   ByRef TextPoint As System.Double, _
   ByVal Val As System.Double, _
   ByVal TextHeight As System.Double _
) As DisplayDimension
```

```

Dim instance As IDrawingDoc
Dim P0 As System.Double
Dim P1 As System.Double
Dim P2 As System.Double
Dim P3 As System.Double
Dim TextPoint As System.Double
Dim Val As System.Double
Dim TextHeight As System.Double
Dim value As DisplayDimension
 
value = instance.ICreateDiamDim4(P0, P1, P2, P3, TextPoint, Val, TextHeight)
```

```

DisplayDimension ICreateDiamDim4( 
   ref System.double P0,
   ref System.double P1,
   ref System.double P2,
   ref System.double P3,
   ref System.double TextPoint,
   System.double Val,
   System.double TextHeight
)
```

```

DisplayDimension^ ICreateDiamDim4( 
   System.double% P0,
   System.double% P1,
   System.double% P2,
   System.double% P3,
   System.double% TextPoint,
   System.double Val,
   System.double TextHeight
) 
```

#### Parameters

*P0*
:   Pointer to an array of 3 doubles (x,y,z); location of dimension point

*P1*
:   Pointer to an array of 3 doubles (x,y,z); nearest point on circle

*P2*
:   Pointer to an array of 3 doubles (x,y,z); farthest point on circle diametrically opposite to P1

*P3*
:   Pointer to an array of 3 doubles (x,y,z); plane normal

*TextPoint*
:   Pointer to an array of 3 doubles (x,y,z); position of text

*Val*
:   Dimension value in meters

*TextHeight*
:   Text height in meters

#### Return Value

Pointer to the new [IDisplayDimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)

Remarks

SOLIDWORKS creates this type of dimension between the two points you specify. It has no relation to your geometry.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IDrawingDoc::CreateLinearDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateLinearDim4.md)  
[IDrawingDoc::CreateDiamDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDiamDim4.md)  
[IDrawingDoc::CreateOrdinateDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateOrdinateDim4.md)  
[IDrawingDoc::ICreateDiamDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateDiamDim4.md)  
[IDrawingDoc::ICreateLinearDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateLinearDim4.md)  
[IDrawingDoc::ICreateOrdinateDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateOrdinateDim4.md)  
[IDrawingDoc::ICreateAngDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateAngDim4.md)  
[IDrawingDoc::CreateAngDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateAngDim4.md)
