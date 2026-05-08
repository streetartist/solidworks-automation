# ISketchPatternFeatureData Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData`

Allows access to a sketch-driven pattern feature in a part.
Allows access to a sketch-driven pattern feature in a part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface ISketchPatternFeatureData 
```

```

Dim instance As ISketchPatternFeatureData
```

```

public interface ISketchPatternFeatureData 
```

```

public interface class ISketchPatternFeatureData 
```

Remarks

Read [Pattern Features and their Feature Data Objects](sldworksapiprogguide.chm::/OVERVIEW/Pattern_Features_and_their_Feature_Data_Objects.htm).

Before calling IFeatureManager::CreateDefinition, you must use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) to pre-select the entities needed to create the circular pattern feature.

To select the required entities, use these selection Marks:

- features = 4
- points = 32
- sketches = 64
- faces = 128
- bodies = 256

You must call [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.md) after initializing this feature data object in order to successfully create a sketch-driven pattern.

For more information, see the **Sketch Driven Patterns** topic in the SOLIDWORKS Help.

Example

[Get Properties of Sketch Pattern Feature (VBA)](Get_Properties_of_Sketch-Pattern_Feature_Example_VB.htm)  
[Get Properties of Sketch Pattern Feature (VB.NET)](Get_Properties_of_Sketch-Pattern_Feature_Example_VBNET.htm)  
[Get Properties of Sketch Pattern Feature (C#)](Get_Properties_of_Sketch-Pattern_Feature_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
