# IGetMiddleSurface Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetMiddleSurface`

Inserts a midsurface in a body.
Inserts a midsurface in a body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetMiddleSurface( _
   ByVal PlacementPercentage As System.Double, _
   ByRef Face1List As System.Object, _
   ByRef Face2List As System.Object, _
   ByRef Thickness As System.Object, _
   ByRef MiddleSurfaceBody As Body2 _
) As System.Integer
```

```

Dim instance As IBody2
Dim PlacementPercentage As System.Double
Dim Face1List As System.Object
Dim Face2List As System.Object
Dim Thickness As System.Object
Dim MiddleSurfaceBody As Body2
Dim value As System.Integer
 
value = instance.IGetMiddleSurface(PlacementPercentage, Face1List, Face2List, Thickness, MiddleSurfaceBody)
```

```

System.int IGetMiddleSurface( 
   System.double PlacementPercentage,
   out System.object Face1List,
   out System.object Face2List,
   out System.object Thickness,
   out Body2 MiddleSurfaceBody
)
```

```

System.int IGetMiddleSurface( 
   System.double PlacementPercentage,
   [Out] System.Object^ Face1List,
   [Out] System.Object^ Face2List,
   [Out] System.Object^ Thickness,
   [Out] Body2^ MiddleSurfaceBody
) 
```

#### Parameters

*PlacementPercentage*
:   Position where to insert the midsurface in the body; value of 50 indicates to insert the surface in the middle

*Face1List*
:   Array of faces into which the midsurface will be or was inserted; you can provide an array of faces for this parameter and Face2List; if you do not, then the faces are determined internally

*Face2List*
:   Array of faces into which the midsurface will be or was inserted; you can provide an array of faces for this parameter and Face1List; if you do not, then the faces are determined internally

*Thickness*
:   Array containing minimum and maximum thickness of sheet metal for pairs of faces

*MiddleSurfaceBody*
:   [Middle surface body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

#### Return Value

0 if no errors; -1 if errors

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IBody2::GetMiddleSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetMiddleSurface.md)
