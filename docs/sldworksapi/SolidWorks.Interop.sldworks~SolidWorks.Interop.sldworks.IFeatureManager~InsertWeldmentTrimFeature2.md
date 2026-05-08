# InsertWeldmentTrimFeature2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertWeldmentTrimFeature2`

Inserts a weldment trim feature for the specified weldment bodies or faces.
Inserts a weldment trim feature for the specified weldment bodies or faces.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertWeldmentTrimFeature2( _
   ByVal EndCond As System.Integer, _
   ByVal Options As System.Integer, _
   ByVal GapValue As System.Double, _
   ByVal BodiesToTrim As System.Object, _
   ByVal BodiesOrFaces As System.Object _
) As Feature
```

```

Dim instance As IFeatureManager
Dim EndCond As System.Integer
Dim Options As System.Integer
Dim GapValue As System.Double
Dim BodiesToTrim As System.Object
Dim BodiesOrFaces As System.Object
Dim value As Feature
 
value = instance.InsertWeldmentTrimFeature2(EndCond, Options, GapValue, BodiesToTrim, BodiesOrFaces)
```

```

Feature InsertWeldmentTrimFeature2( 
   System.int EndCond,
   System.int Options,
   System.double GapValue,
   System.object BodiesToTrim,
   System.object BodiesOrFaces
)
```

```

Feature^ InsertWeldmentTrimFeature2( 
   System.int EndCond,
   System.int Options,
   System.double GapValue,
   System.Object^ BodiesToTrim,
   System.Object^ BodiesOrFaces
) 
```

#### Parameters

*EndCond*
:   End condition as defined by [swSolidworksWeldmentEndCondOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSOLIDWORKSWeldmentEndCondOptions_e.html)

*Options*
:   Logical sum of values as defined in [swWeldmentTrimExtendOptionType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWeldmentTrimExtendOptionType_e.html) (see **Remarks**)

*GapValue*
:   Length to trim (see **Remarks**)

*BodiesToTrim*
:   Array of bodies to trim

*BodiesOrFaces*
:   Array of bodies or faces that define the trimming boundaries

#### Return Value

[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

Use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) and specify the following marks to select the body, or bodies, to trim and the trimming boundaries:

- 1 = Body or bodies to trim
- 2 = Trimming boundaries (body or face)

If you include swWeldmentTrimExtendOption\_WeldGap in the Options parameter, then the GapValue parameter is used. Specify 0 for GapValue to ensure that there is no weld gap.

If you exclude swWeldmentTrimExtendOption\_WeldGap from the Options parameter, then the weld gap defaults to the last value specified in the SOLIDWORKS user-interface.

Example

[Insert Weldment Features (VBA)](Insert_Weldment_Features_Example_VB.htm)  
[Insert Weldment Features (VB.NET)](Insert_Weldment_Features_Example_VBNET.htm)  
[Insert Weldment Features (C#)](Insert_Weldment_Features_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IFeatureManager::InsertWeldmentTrimFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertWeldmentTrimFeature.md)  
[IWeldmentTrimExtendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData.md)
