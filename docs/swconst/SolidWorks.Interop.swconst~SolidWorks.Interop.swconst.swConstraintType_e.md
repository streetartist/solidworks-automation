# swConstraintType_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swConstraintType_e`

Sketch constraints.
Sketch constraints.

Syntax

- [Visual Basic](#Syntax-VBAll)
- [C#](#Syntax-CS)
- [Delphi](#Syntax-Delphi)
- [JScript](#Syntax-JScript)
- [Managed Extensions for C++](#Syntax-CPP)
- [C++/CLI](#Syntax-CPP2005)

```

'Declaration
 
```

```

<System.Runtime.InteropServices.GuidAttribute("77E7ABFB-C9AA-4C6A-AC14-05F1AEC611AD")>
Public Enum swConstraintType_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swConstraintType_e
```

```

[System.Runtime.InteropServices.Guid("77E7ABFB-C9AA-4C6A-AC14-05F1AEC611AD")]
public enum swConstraintType_e : System.Enum 
```

```

public enum swConstraintType_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("77E7ABFB-C9AA-4C6A-AC14-05F1AEC611AD")
public enum swConstraintType_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("77E7ABFB-C9AA-4C6A-AC14-05F1AEC611AD")]
__value public enum swConstraintType_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("77E7ABFB-C9AA-4C6A-AC14-05F1AEC611AD")]
public enum class swConstraintType_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swConstraintType\_ALONGX** | 48 |
| **swConstraintType\_ALONGX3D** | 64 |
| **swConstraintType\_ALONGXPOINTS** | 51 |
| **swConstraintType\_ALONGXPOINTS3D** | 66 |
| **swConstraintType\_ALONGY** | 49 |
| **swConstraintType\_ALONGY3D** | 65 |
| **swConstraintType\_ALONGYPOINTS** | 52 |
| **swConstraintType\_ALONGYPOINTS3D** | 67 |
| **swConstraintType\_ALONGZ** | 50 |
| **swConstraintType\_ALONGZPOINTS** | 53 |
| **swConstraintType\_ANGLE** | 2 |
| **swConstraintType\_ANGLE3P** | 43 |
| **swConstraintType\_ARCANG180** | 19 |
| **swConstraintType\_ARCANG270** | 20 |
| **swConstraintType\_ARCANG90** | 18 |
| **swConstraintType\_ARCANGBOTTOM** | 22 |
| **swConstraintType\_ARCANGLEFT** | 23 |
| **swConstraintType\_ARCANGRIGHT** | 24 |
| **swConstraintType\_ARCANGTOP** | 21 |
| **swConstraintType\_ARCLENGTH** | 44 |
| **swConstraintType\_ATINTERSECT** | 13 |
| **swConstraintType\_ATMIDDLE** | 12 |
| **swConstraintType\_ATPIERCE** | 40 |
| **swConstraintType\_BELTTRACTION** | 69 |
| **swConstraintType\_BLOCKFIXEDLOCK** | 70 = Lock two blocks together |
| **swConstraintType\_BLOCKNORMALLOCK** | 71 = Lock blocks to be normal to one another (3D sketch) |
| **swConstraintType\_BLOCKROTATELOCK** | 72 = Lock blocks to rotate around each other (3D sketch) |
| **swConstraintType\_C3TOUCH** | 83 |
| **swConstraintType\_CIRCULARPATTCNT** | 77 |
| **swConstraintType\_COINCIDENT** | 9 |
| **swConstraintType\_COLINEAR** | 27 |
| **swConstraintType\_CONCENTRIC** | 10 |
| **swConstraintType\_CONICRHO** | 82 |
| **swConstraintType\_CORADIAL** | 28 |
| **swConstraintType\_DIAMETER** | 15 |
| **swConstraintType\_DISTANCE** | 1 |
| **swConstraintType\_DOUBLEANGLE** | 84 = Double angle display |
| **swConstraintType\_DOUBLEDISTANCE** | 41 |
| **swConstraintType\_ELLIPSEANG180** | 34 |
| **swConstraintType\_ELLIPSEANG270** | 35 |
| **swConstraintType\_ELLIPSEANG90** | 33 |
| **swConstraintType\_ELLIPSEANGBOTTOM** | 37 |
| **swConstraintType\_ELLIPSEANGLEFT** | 38 |
| **swConstraintType\_ELLIPSEANGRIGHT** | 39 |
| **swConstraintType\_ELLIPSEANGTOP** | 36 |
| **swConstraintType\_EQUALCURV3DALIGN** | 80 =  Aligned equal curvature between 3D splines |
| **swConstraintType\_EQUALCURVATURE** | 61 |
| **swConstraintType\_EQUALTANGENT** | 62 |
| **swConstraintType\_FAKESLOTCONSTRAINT** | 73 = Not actually a constraint; for display purposes only |
| **swConstraintType\_FITSPLINE** | 60 |
| **swConstraintType\_FIXED** | 17 |
| **swConstraintType\_FIXEDSLOT** | 74 = Fix a slot |
| **swConstraintType\_FLANGEFACEDIST** | 81 = Distance from virtual point to the relevant flange face |
| **swConstraintType\_HORIZONTAL** | 4 |
| **swConstraintType\_HORIZPOINTS** | 25 |
| **swConstraintType\_INTERSECTION** | 56 |
| **swConstraintType\_INVALIDCTYPE** | 0 |
| **swConstraintType\_ISOBYPOINT** | 58 = ISO curve when its constraint parameter is determined by an external point |
| **swConstraintType\_LINEARPATTCNT** | 76 |
| **swConstraintType\_MERGEPOINTS** | 42 |
| **swConstraintType\_NORMAL** | 45 |
| **swConstraintType\_NORMALPOINTS** | 46 |
| **swConstraintType\_OFFSETEDGE** | 16 |
| **swConstraintType\_PARALLEL** | 7 |
| **swConstraintType\_PARALLELYZ** | 54 |
| **swConstraintType\_PARALLELZX** | 55 |
| **swConstraintType\_PATTERNED** | 57 |
| **swConstraintType\_PERPENDICULAR** | 8 |
| **swConstraintType\_PLANAROFFSET** | 79 = For routing pipe offsets |
| **swConstraintType\_RADIALOFFSET** | 78 = For routing pipe offsets |
| **swConstraintType\_RADIUS** | 3 |
| **swConstraintType\_SAMECURVELENGTH** | 85 = Equal arc/spline length |
| **swConstraintType\_SAMEISOPARAM** | 59 = Common relation for all pieces ( for the face ) of the surface's iso curve |
| **swConstraintType\_SAMELENGTH** | 14 |
| **swConstraintType\_SAMESLOTS** | 75 = Same slot width and length |
| **swConstraintType\_SKETCHOFFSET** | 47 = Between entities of the same sketch |
| **swConstraintType\_SNAPANGLE** | 31 |
| **swConstraintType\_SNAPGRID** | 29 |
| **swConstraintType\_SNAPLENGTH** | 30 |
| **swConstraintType\_SYMMETRIC** | 11 |
| **swConstraintType\_TANGENT** | 6 |
| **swConstraintType\_TANGENTFACE** | 63 |
| **swConstraintType\_TRACTION** | 68 |
| **swConstraintType\_USEEDGE** | 32 |
| **swConstraintType\_VERTICAL** | 5 = Applies only to sketch lines |
| **swConstraintType\_VERTPOINTS** | 26 = Applies only to sketch points |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swConstraintType\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
