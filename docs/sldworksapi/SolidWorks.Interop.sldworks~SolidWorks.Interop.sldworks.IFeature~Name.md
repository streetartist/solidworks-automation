# Name Property (IFeature)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Name`

Gets or sets the name of the current feature.
Gets or sets the name of the current feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Name As System.String
```

```

Dim instance As IFeature
Dim value As System.String
 
instance.Name = value
 
value = instance.Name
```

```

System.string Name {get; set;}
```

```

property System.String^ Name {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Name of the feature

Remarks

Feature names can be seen in the FeatureManager design tree of any part or assembly.

Any change to a feature name is not visible to the user until a rebuild has been done. See [IModelDoc2::EditRebuild3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRebuild3.md).

If you are setting the name of a feature, then the new name must be unique in the FeatureManager design tree. If the name is not unique, then the name is not changed. Also, the name cannot contain characters that are reserved by SOLIDWORKS.

Example

[Access Assembly (C++)](Access_Assembly_Example_CPlusPlus_COM.htm)  
[Get Parent Features (C++)](Get_Parent_Features_Example_CPlusPlus_COM.htm)  
[Get Selected Feature (C++)](Get_Selected_Feature_Example_CPlusPlus_COM.htm)  
[Get Sketches (C++)](Get_Sketches_Example_CPlusPlus_COM.htm)  
[Find Total Length of Sketch Segments in Sketch (VBA)](Find_Total_Length_of_Sketch_Segments_in_Sketch_Example_VB.htm)  
[Get Section Properties for Faces from Section Planes (VBA)](Get_Section_Properties_Example_VB.htm)  
[Traverse Assembly at Component and Feature Levels Using Recursion (VB.NET)](Traverse_Assembly_at_Component_and_Feature_Levels_Using_Recursion_Example_VBNET.htm)  
[Traverse Assembly at Component and Feature Levels Using Recursion (C#)](Traverse_Assembly_at_Component_and_Feature_Levels_Using_Recursion_Example_CSharp.htm)  
[Traverse Assembly at Component and Feature Levels Using Recursion (VBA)](Traverse_Assembly_at_Component_and_Feature_Levels_Using_Recursion_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)  
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.md)  
[IFeature::GetNameForSelection Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetNameForSelection.md)
