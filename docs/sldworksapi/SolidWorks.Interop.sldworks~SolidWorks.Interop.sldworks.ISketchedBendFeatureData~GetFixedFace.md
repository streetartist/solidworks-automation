# GetFixedFace Method (ISketchedBendFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData~GetFixedFace`

Gets the fixed face from this sketched bend.
Gets the fixed face from this sketched bend.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFixedFace( _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double _
) As System.Object
```

```

Dim instance As ISketchedBendFeatureData
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Object
 
value = instance.GetFixedFace(X, Y, Z)
```

```

System.object GetFixedFace( 
   out System.double X,
   out System.double Y,
   out System.double Z
)
```

```

System.Object^ GetFixedFace( 
   [Out] System.double X,
   [Out] System.double Y,
   [Out] System.double Z
) 
```

#### Parameters

*X*
:   X location

*Y*
:   Y location

*Z*
:   Z location

#### Return Value

Fixed [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) that does not move as a result of the bend

Remarks

The location is a point on the fixed face, but in the space of the sketch used to define the sketched-bend feature. Thus, the z location is always 0.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Example

[Change Bend Radius of Sketched Bend (VBA)](Change_Bend_Radius_of_Sketched_Bend_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchedBendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData.md)  
[ISketchedBendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData_members.md)  
[ISketchedBendFeatureData::SetFixedFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData~SetFixedFace.md)
