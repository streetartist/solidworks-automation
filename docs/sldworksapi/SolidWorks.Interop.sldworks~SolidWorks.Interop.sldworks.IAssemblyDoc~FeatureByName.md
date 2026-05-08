# FeatureByName Method (IAssemblyDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~FeatureByName`

Returns the IFeature object for the named feature in the assembly.
Returns the [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) object for the named feature in the assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function FeatureByName( _
   ByVal Name As System.String _
) As System.Object
```

```

Dim instance As IAssemblyDoc
Dim Name As System.String
Dim value As System.Object
 
value = instance.FeatureByName(Name)
```

```

System.object FeatureByName( 
   System.string Name
)
```

```

System.Object^ FeatureByName( 
   System.String^ Name
) 
```

#### Parameters

*Name*
:   Name of the feature

#### Return Value

Object for the feature

Example

[Get Parent-Child Relationship for Component (VBA)](Get_Parent-Child_Relationship_for_Component_Example_VB.htm)  
[Create and Name Plane (VBA)](Create_and_Name_Plane_Example_VB.htm)  
[Move Assembly Components to New Folder (C#)](Move_Assembly_Components_to_New_Folder_Example_CSharp.htm)  
[Move Assembly Components to New Folder (VB.NET)](Move_Assembly_Components_to_New_Folder_Example_VBNET.htm)  
[Move Assembly Components to New Folder (VBA)](Move_Assembly_Components_to_New_Folder_Example_VB.htm)  
[Roll Back Model (C#)](Roll_Back_Model_Example_CSharp.htm)  
[Roll Back Model (VB.NET)](Roll_Back_Model_Example_VBNET.htm)  
[Roll Back Model (VBA)](Roll_Back_Model_Example_VB.htm)  
[Suppress Component Feature (C#)](Suppress_Component_Feature_Example_CSharp.htm)  
[Suppress Component Feature (VB.NET)](Suppress_Component_Feature_Example_VBNET.htm)  
[Suppress Component Feature (VBA)](Suppress_Component_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::IFeatureByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IFeatureByName.md)
