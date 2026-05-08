# SetSmartComponentData Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetSmartComponentData`

Sets the features, components, and feature references of a Smart Component.
Sets the features, components, and feature references of a Smart Component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetSmartComponentData( _
   ByVal FeaturesSelected As System.Object, _
   ByVal ComponentsSelected As System.Object, _
   ByVal References As System.Object _
) As System.Boolean
```

```

Dim instance As IComponent2
Dim FeaturesSelected As System.Object
Dim ComponentsSelected As System.Object
Dim References As System.Object
Dim value As System.Boolean
 
value = instance.SetSmartComponentData(FeaturesSelected, ComponentsSelected, References)
```

```

System.bool SetSmartComponentData( 
   System.object FeaturesSelected,
   System.object ComponentsSelected,
   System.object References
)
```

```

System.bool SetSmartComponentData( 
   System.Object^ FeaturesSelected,
   System.Object^ ComponentsSelected,
   System.Object^ References
) 
```

#### Parameters

*FeaturesSelected*
:   Array of boolean values indicating which features to enable in the Smart Component (see **Remarks**)

*ComponentsSelected*
:   Array of boolean values indicating which components to enable in the Smart Component (see **Remarks**)

*References*
:   Array of feature reference entities in the target assembly that are used to activate the features specified by FeaturesSelected (see **Remarks**)

#### Return Value

True if successful, false if not

Remarks

A Smart Component is defined by its:

- Components
- Features
- Feature references

See the SOLIDWORKS Help for more information about Smart Components.

Use this method to:

- Change which features and components to enable in a Smart Component.
- Activate the Smart Features.

Before calling this method:

1. Open an assembly that contains a Smart Component whose Smart Features have not yet been activated.
2. Find the Smart Component in the assembly using [IComponent2::IsSmartComponent](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsSmartComponent.md).
3. Call [IComponent2::GetSmartComponentData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetSmartComponentData.md) to obtain the current feature and component arrays for the Smart Component.
4. Create two boolean arrays whose elements map one-to-one with the elements in the feature and component arrays.
5. For each element in each boolean array, specify true if the corresponding feature or component is enabled in the Smart Component. Specify false if it is not.
6. Set FeaturesSelected and ComponentsSelected with the corresponding boolean arrays.
7. Create an array of reference entities (e.g., faces, edges, points) selected from the target assembly that map to the feature reference entities that were defined for the Smart Component.
8. Set References to the array of reference entities.

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
