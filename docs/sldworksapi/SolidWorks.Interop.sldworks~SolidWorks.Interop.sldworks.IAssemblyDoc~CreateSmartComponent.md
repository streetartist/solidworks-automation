# CreateSmartComponent Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateSmartComponent`

Creates a Smart Component.
Creates a Smart Component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateSmartComponent( _
   ByVal ComponentIn As Component2, _
   ByVal RelatedComponents As System.Object, _
   ByVal RelatedFeatures As System.Object, _
   ByVal AutoSizeDiameter As System.Boolean, _
   ByVal LpMateReference As Entity, _
   ByVal BoundingValues As System.Object _
) As System.Boolean
```

```

Dim instance As IAssemblyDoc
Dim ComponentIn As Component2
Dim RelatedComponents As System.Object
Dim RelatedFeatures As System.Object
Dim AutoSizeDiameter As System.Boolean
Dim LpMateReference As Entity
Dim BoundingValues As System.Object
Dim value As System.Boolean
 
value = instance.CreateSmartComponent(ComponentIn, RelatedComponents, RelatedFeatures, AutoSizeDiameter, LpMateReference, BoundingValues)
```

```

System.bool CreateSmartComponent( 
   Component2 ComponentIn,
   System.object RelatedComponents,
   System.object RelatedFeatures,
   System.bool AutoSizeDiameter,
   Entity LpMateReference,
   System.object BoundingValues
)
```

```

System.bool CreateSmartComponent( 
   Component2^ ComponentIn,
   System.Object^ RelatedComponents,
   System.Object^ RelatedFeatures,
   System.bool AutoSizeDiameter,
   Entity^ LpMateReference,
   System.Object^ BoundingValues
) 
```

#### Parameters

*ComponentIn*
:   [IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) to make smart

*RelatedComponents*
:   Array of the components to associate with the Smart Component

*RelatedFeatures*
:   Array of the [features](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) contained in the components to associate with the Smart Component

*AutoSizeDiameter*
:   True to auto-size a cylindrical Smart Component that has multiple configurations, false to not

*LpMateReference*
:   Concentric mate reference between a cylindrical face or axis and a feature

*BoundingValues*
:   Array of doubles specifying minimum and maximum diameter values with which each configuration is compatible

#### Return Value

True if the Smart Component is created, false if not

Remarks

For example, a component with these configurations:

- TenInchDiameter
- ThirteenInchDiameter
- TwentyInchDiameter

might have a BoundingValues array of [9,11,12,14,19,21], which specifies a +1 tolerance over each configuration parameter.

Example

[Make Smart Component (VBA)](Make_Smart_Component_Example_VB.htm)  
[Make Smart Component With Mate (VBA)](Make_Smart_Component_with__Mate_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::AddSmartComponent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddSmartComponent.md)  
[IComponent2::GetSmartComponentData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetSmartComponentData.md)  
[IComponent2::IsSmartComponent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsSmartComponent.md)  
[IComponent2::SetSmartComponentData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetSmartComponentData.md)  
[ISmartComponentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISmartComponentFeatureData.md)
