# GetComponents Method (IAssemblyDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetComponents`

Gets all of the components in the active configuration of this assembly.
Gets all of the components in the active configuration of this assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetComponents( _
   ByVal ToplevelOnly As System.Boolean _
) As System.Object
```

```

Dim instance As IAssemblyDoc
Dim ToplevelOnly As System.Boolean
Dim value As System.Object
 
value = instance.GetComponents(ToplevelOnly)
```

```

System.object GetComponents( 
   System.bool ToplevelOnly
)
```

```

System.Object^ GetComponents( 
   System.bool ToplevelOnly
) 
```

#### Parameters

*ToplevelOnly*
:   True to get only the top-level components of the FeatureManager design tree, false to get both the top-level and child components in the FeatureManager design tree

#### Return Value

Array of [IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)s (see **Remarks**)

Remarks

The components returned by this method can be in any order. You should not rely on the order to indicate anything about children or parents. If the hierarchy and order are important, then use [IModelDoc2::FirstFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FirstFeature.md), [IFeature::GetTypeName2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetTypeName2.md), [IFeature::GetSpecificFeature2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetSpecificFeature2.md), [IComponent2::FirstFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~FirstFeature.md), and [IFeature::GetNextFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetNextFeature.md) to retrieve your information.

Example

[Insert MidSurface in Components (C#)](Insert_MidSurface_in_Component_Example_CSharp.htm)  
[Insert MidSurface in Component (VB.NET)](Insert_MidSurface_in_Component_Example_VBNET.htm)  
[Insert MidSurface in Component (VBA)](Insert_MidSurface_in_Component_Example_VB.htm)  
[Get Mates (VB.NET)](Get_Mates_Example_VBNET.htm)  
[Get Mates (C#)](Get_Mates_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::IGetComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IGetComponents.md)  
[IAssemblyDoc::GetComponentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetComponentCount.md)  
[IComponent2::GetChildren Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetChildren.md)  
[IComponent2::GetParent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetParent.md)  
[IConfiguration::GetRootComponent3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetRootComponent3.md)  
[IConfiguration::IGetRootComponent2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetRootComponent2.md)  
[IConfigurationManager::ActiveConfiguration Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~ActiveConfiguration.md)  
[IAssemblyDoc::SelectiveOpen Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SelectiveOpen.md)  
[IAssemblyDoc::GetComponentByID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetComponentByID.md)
