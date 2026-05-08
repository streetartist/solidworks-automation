# AddCornerReliefType Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~AddCornerReliefType`

Specifies the type of corner relief to apply to the specified corner of the selected sheet metal body.
Specifies the type of corner relief to apply to the specified corner of the selected sheet metal body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddCornerReliefType( _
   ByVal CornerIndex As System.Integer, _
   ByVal ReliefType As System.Integer, _
   ByVal Length1 As System.Double, _
   ByVal Length2 As System.Double, _
   ByVal Length3 As System.Double, _
   ByVal CenterOnBendLines As System.Boolean, _
   ByVal RatioToThickness As System.Boolean, _
   ByVal TangentToBend As System.Boolean, _
   ByVal AddFilletedCorners As System.Boolean, _
   ByVal NarrowCorner As System.Boolean _
) As System.Boolean
```

```

Dim instance As IFeatureManager
Dim CornerIndex As System.Integer
Dim ReliefType As System.Integer
Dim Length1 As System.Double
Dim Length2 As System.Double
Dim Length3 As System.Double
Dim CenterOnBendLines As System.Boolean
Dim RatioToThickness As System.Boolean
Dim TangentToBend As System.Boolean
Dim AddFilletedCorners As System.Boolean
Dim NarrowCorner As System.Boolean
Dim value As System.Boolean
 
value = instance.AddCornerReliefType(CornerIndex, ReliefType, Length1, Length2, Length3, CenterOnBendLines, RatioToThickness, TangentToBend, AddFilletedCorners, NarrowCorner)
```

```

System.bool AddCornerReliefType( 
   System.int CornerIndex,
   System.int ReliefType,
   System.double Length1,
   System.double Length2,
   System.double Length3,
   System.bool CenterOnBendLines,
   System.bool RatioToThickness,
   System.bool TangentToBend,
   System.bool AddFilletedCorners,
   System.bool NarrowCorner
)
```

```

System.bool AddCornerReliefType( 
   System.int CornerIndex,
   System.int ReliefType,
   System.double Length1,
   System.double Length2,
   System.double Length3,
   System.bool CenterOnBendLines,
   System.bool RatioToThickness,
   System.bool TangentToBend,
   System.bool AddFilletedCorners,
   System.bool NarrowCorner
) 
```

#### Parameters

*CornerIndex*
:   Index of corner to which to apply the corner relief; -1 to apply it to the corner last added with [IFeatureManager::AddCornerReliefCorner](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~AddCornerReliefCorner.md)

*ReliefType*
:   Type of corner relief as defined by [swCornerReliefType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCornerReliefType_e.html)

*Length1*
:   Not used

*Length2*
:   | If ReliefType is swCornerReliefType\_e... | Then Length2 is the slot... |
    | --- | --- |
    | swCornerSquareRelief | Length of the corner relief |
    | swCornerObroundRelief | Length of the corner relief |
    | swCornerCircularRelief | Radius of the corner relief |

*Length3*
:   | If ReliefType is swCornerReliefType\_e... | Then Length3 is... |
    | --- | --- |
    | swCornerObroundRelief | Slot width of the corner relief |
    | swCornerSquareRelief and FilletedCorners = true | Radius of filleted corner |

*CenterOnBendLines*
:   True to center the corner relief relative to the bend lines, false to not; valid only if ReliefType is one of the following:

    - swCornerReliefType\_e.swCornerSquareRelief
    - swCornerReliefType\_e.swCornerCircularRelief
    - swCornerReliefType\_e.swCornerObroundRelief

*RatioToThickness*
:   True to use a ratio value to cut the bend area so that the body can be folded, false to not; the ratios for valid relief types are calculated as follows where t = thickness of sheet metal:

    | If ReliefType is swCornerReliefType\_e... | Then ratios are... |
    | --- | --- |
    | swCornerSquareRelief | Length2/t |
    | swCornerCircularRelief | Length2/t |
    | swCornerObroundRelief | Length2/t and Length3/t |

*TangentToBend*
:   True to make the corner relief tangent to the inside bend edges, false to not

*AddFilletedCorners*
:   True to fillet the corner relief corners, false to not; valid only if ReliefType = swCornerReliefType\_e.swCornerSquareRelief

*NarrowCorner*
:   True to use the algorithm for large bend radii to narrow the corner relief in the bend area, false to not; valid only if ReliefType is one of the following:

    - swCornerReliefType\_e.swCornerSquareRelief
    - swCornerReliefType\_e.swCornerCircularRelief
    - swCornerReliefType\_e.swCornerObroundRelief

#### Return Value

True if successful, false if not

Remarks

To create a corner relief feature:

1. Call [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) with Mark = 0 and Append = true to select the sheet metal body in which to create a corner relief feature.
2. Call IModelDocExtension::SelectByID2 with Mark = 4 and Append = true to select two faces that form a bend corner.
3. Call [IFeatureManager::AddCornerReliefCorner](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~AddCornerReliefCorner.md) to add the corner to the corner relief feature.
4. Call this method to specify the corner relief for the corner.
5. Repeat steps 2 - 4 to add another corner to the corner relief feature.
6. Call [IFeatureManager::FinishCornerRelief](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FinishCornerRelief.md).

Example

[Create Corner Relief Feature (C#)](Create_Corner_Relief_Feature_Example_CSharp.htm)  
[Create Corner Relief Feature (VBA)](Create_Corner_Relief_Feature_Example_VB.htm)  
[Create Corner Relief Feature (VB.NET)](Create_Corner_Relief_Feature_Example_VBNET.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IFlatPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData.md)
