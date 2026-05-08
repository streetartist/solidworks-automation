# swTwistControlType_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTwistControlType_e`

Sweep twist control options.
Sweep twist control options.

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

<System.Runtime.InteropServices.GuidAttribute("BA2E3CB6-4988-458F-A0C8-BC4ECE0EDB8E")>
Public Enum swTwistControlType_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swTwistControlType_e
```

```

[System.Runtime.InteropServices.Guid("BA2E3CB6-4988-458F-A0C8-BC4ECE0EDB8E")]
public enum swTwistControlType_e : System.Enum 
```

```

public enum swTwistControlType_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("BA2E3CB6-4988-458F-A0C8-BC4ECE0EDB8E")
public enum swTwistControlType_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("BA2E3CB6-4988-458F-A0C8-BC4ECE0EDB8E")]
__value public enum swTwistControlType_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("BA2E3CB6-4988-458F-A0C8-BC4ECE0EDB8E")]
public enum class swTwistControlType_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swTwistControlConstantTwistAlongPath** | 8 = Defines the twist of the profile along the sweep path; corresponds to **Profile Twist > Specify Twist Value** in the Sweep PropertyManager |
| **swTwistControlFollowFirstSecondGuideCurves** | 3 = The twist of the intermediate sections is determined by the vector from the first guide cruve to the second guide curve; the angle between the horizontal plane and the vector remains constant in the sketch planes of all of the intermediate sections; corresponds to **Profile Twist > Follow First and Second Guide Curves** in the Sweep PropertyManager (only valid if two guide curves are present) |
| **swTwistControlFollowPath** | 0 = Corresponds to **Profile orientation > Follow Path** in the Sweep PropertyManager; after specifying this option, use [ISweepFeatureData::PathAlignmentType](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~PathAlignmentType.html) to specify path alignment options as defined in [swTangencyType\_e](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTangencyType_e.md) |
| **swTwistControlFollowPathFirstGuideCurve** | 2 = The twist of the intermediate sections is determined by the vector from the path to the first guide curve; the angle between the horizontal plane and the vector remains constant in the sketch planes of all of the intermediate sections; corresponds to **Profile Twist > Follow Path and First Guide Curve** in the Sweep PropertyManager (only valid if at least one guide curve is present) |
| **swTwistControlKeepNormalConstant** | 1 = Twists the section along the sweep path, keeping the section parallel to the beginning section as it twists along the path; corresponds to **Profile orientation > Keep Normal Constant** in the Sweep PropertyManager |
| **swTwistControlNormalConstantTwistAlongPath** | 9 = Defines the twist of the profile along the sweep path, keeping the section parallel to the beginning section as it twists along the path; corresponds to **Profile orientation > Keep Normal Constant** and **Profile Twist > Specify Twist Value** in the Sweep PropertyManager |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swTwistControlType\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
