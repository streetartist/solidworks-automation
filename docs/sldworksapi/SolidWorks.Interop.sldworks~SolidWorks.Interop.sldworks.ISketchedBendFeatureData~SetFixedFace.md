# SetFixedFace Method (ISketchedBendFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData~SetFixedFace`

Sets the fixed face of this sketched bend.
Sets the fixed face of this sketched bend.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetFixedFace( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double, _
   ByVal EdgeArray As System.Object _
) 
```

```

Dim instance As ISketchedBendFeatureData
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim EdgeArray As System.Object
 
instance.SetFixedFace(X, Y, Z, EdgeArray)
```

```

void SetFixedFace( 
   System.double X,
   System.double Y,
   System.double Z,
   System.object EdgeArray
)
```

```

void SetFixedFace( 
   System.double X,
   System.double Y,
   System.double Z,
   System.Object^ EdgeArray
) 
```

#### Parameters

*X*
:   X location

*Y*
:   Y location

*Z*
:   Z location

*EdgeArray*
:   Array of edges

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchedBendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData.md)  
[ISketchedBendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData_members.md)  
[ISketchedBendFeatureData::GetFixedFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData~GetFixedFace.md)
