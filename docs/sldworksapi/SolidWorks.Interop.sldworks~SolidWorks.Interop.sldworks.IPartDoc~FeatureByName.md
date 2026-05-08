# FeatureByName Method (IPartDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~FeatureByName`

Gets the named feature in the part.
Gets the named feature in the part.

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

Dim instance As IPartDoc
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
:   Name of feature

#### Return Value

[Feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Example

[Autodimension All Sketches (VBA)](Autodimension_All_Sketches_Example_VB.htm)  
[Get and Set Constraint for Dome Feature (VBA)](Get_and_Set_Constraint_for_Dome_Feature_Example_VB.htm)  
[Move Copy Sketch Entities (C#)](Move_Copy_Sketch_Entities_Example_CSharp.htm)  
[Move Copy Sketch Entities (VB.NET)](Move_Copy_Sketch_Entities_Example_VBNET.htm)  
[Move Copy Sketch Entities (VBA)](Move_Copy_Sketch_Entities_Example_VB.htm)  
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

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)  
[IPartDoc::IFeatureByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IFeatureByName.md)  
[IPartDoc::IFeatureById Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IFeatureById.md)  
[IPartDoc::FeatureById Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~FeatureById.md)  
[IAssemblyDoc::FeatureByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~FeatureByName.md)  
[IAssemblyDoc::IFeatureByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IFeatureByName.md)  
[IComponent2::FeatureByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~FeatureByName.md)  
[IDrawingDoc::FeatureByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~FeatureByName.md)  
[IDrawingDoc::IFeatureByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IFeatureByName.md)
