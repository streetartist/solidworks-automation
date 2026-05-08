# GetSmartComponentData Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetSmartComponentData`

Gets the features, components, and feature references of a Smart Component.
Gets the features, components, and feature references of a Smart Component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSmartComponentData( _
   ByRef Features As System.Object, _
   ByRef FeaturesSelected As System.Object, _
   ByRef Components As System.Object, _
   ByRef ComponentsSelected As System.Object, _
   ByRef References As System.Object _
) As System.Boolean
```

```

Dim instance As IComponent2
Dim Features As System.Object
Dim FeaturesSelected As System.Object
Dim Components As System.Object
Dim ComponentsSelected As System.Object
Dim References As System.Object
Dim value As System.Boolean
 
value = instance.GetSmartComponentData(Features, FeaturesSelected, Components, ComponentsSelected, References)
```

```

System.bool GetSmartComponentData( 
   out System.object Features,
   out System.object FeaturesSelected,
   out System.object Components,
   out System.object ComponentsSelected,
   out System.object References
)
```

```

System.bool GetSmartComponentData( 
   [Out] System.Object^ Features,
   [Out] System.Object^ FeaturesSelected,
   [Out] System.Object^ Components,
   [Out] System.Object^ ComponentsSelected,
   [Out] System.Object^ References
) 
```

#### Parameters

*Features*
:   Array of [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)s that can be selected for this Smart Component (see **Remarks**)

*FeaturesSelected*
:   Array of boolean values; true if the corresponding item in the Features array is selected, false if it is not selected

*Components*
:   Array of [IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)s that can be selected for this Smart Component (see **Remarks**)

*ComponentsSelected*
:   Array of boolean values; true if the corresponding item in the Components array is selected, false if it is not selected

*References*
:   Array of feature reference entities that are used to activate the Smart Features specified by Features and FeaturesSelected; empty if the Smart Component features have not been activated (see **Remarks**)

#### Return Value

True if successful, false if not

Remarks

A Smart Component is defined by:

- Components
- Features
- Feature references

See the SOLIDWORKS Help for more information about Smart Components.

Use this method to get the current features, components, and feature references of a Smart Component.

Before calling this method:

1. Open an assembly that contains a Smart Component whose Smart Features are not activated.
2. Find the Smart Component in the assembly using [IComponent2::IsSmartComponent](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsSmartComponent.md).

After calling this method, use [IComponent2::SetSmartComponentData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetSmartComponentData.md) to change which features and components of a Smart Component to enable and which Smart Features to activate.

Use [ISmartComponentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISmartComponentFeatureData.md) to:

- Insert new features and components into a Smart Component.
- Delete features and components from a Smart Component.

Example

[Activate Smart Features in an Assembly (VBA)](Activate_Smart_Features_in_an_Assembly_Example_VB.htm)  
[Activate Smart Features in an Assembly (VB.NET)](Activate_Smart_Features_in_an_Assembly_Example_VBNET.htm)  
[Activate Smart Features in an Assembly (C#)](Activate_Smart_Features_in_an_Assembly_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IAssemblyDoc::AddSmartComponent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddSmartComponent.md)  
[IAssemblyDoc::CreateSmartComponent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateSmartComponent.md)
