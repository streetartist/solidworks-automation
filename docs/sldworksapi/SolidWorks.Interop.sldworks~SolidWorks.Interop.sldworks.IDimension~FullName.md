# FullName Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~FullName`

Gets the full name of a dimension including the feature and the model.
Gets the full name of a dimension including the feature and the model.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property FullName As System.String
```

```

Dim instance As IDimension
Dim value As System.String
 
value = instance.FullName
```

```

System.string FullName {get;}
```

```

property System.String^ FullName {
   System.String^ get();
}
```

#### Property Value

Name of the dimension including the feature and model

Remarks

The syntax of the name returned is:

<Dimension Name>@<Feature Name>@<Model>

where:

- <Dimension Name> is the name of the dimension as returned from [IDimension::Name](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~Name.md)
- <Feature Name> is the name of the feature that the dimension is on
- <Model> is the name of the model containing the feature

For example:

"D1@Sketch1@Part4.Part"

Example

[Determine if Display Dimension Marked for Drawing (VBA)](Determine_if_Display_Dimension_Marked_for_Drawing_Example_VB.htm)  
[Get Block Information (VBA)](Get_Block_Information_Example_VB.htm)  
[Get Dimension Values in All Configurations (VBA)](Get_Dimension_Values_in_All_Configurations_Example_VB.htm)  
[Get Mate Definition (VBA)](Get_Mate_Definition_Example_VB.htm)  
[Iterate Through Dimensions in Model (VBA)](Iterate_Through_Dimensions_in_Model_Example_VB.htm)  
[Set Dimensions to Mid-tolerance (VBA)](Set_Dimensions_to_Mid-Tolerance_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.md)  
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.md)
