# EnumRelatedBodies Method (IComponent2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~EnumRelatedBodies`

Creates an enumerated list of bodies.
Creates an enumerated list of bodies.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function EnumRelatedBodies() As EnumBodies2
```

```

Dim instance As IComponent2
Dim value As EnumBodies2
 
value = instance.EnumRelatedBodies()
```

```

EnumBodies2 EnumRelatedBodies()
```

```

EnumBodies2^ EnumRelatedBodies(); 
```

#### Return Value

Pointer to the [enumerated list of bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumBodies2.md)

Remarks

The list contains only those bodies associated with reference surfaces. You get a list of bodies that are related to the model, but the list does not include the part body itself.

A reference surface feature might consist of one or more surfaces sewn together. SOLIDWORKS represents each reference surface feature with two bodies: one to represent the front faces and one to represent the back faces. Each IBody2 object has one or more faces depending on whether the reference surface feature is a set of sewn surfaces or a single underlying surface. The corresponding faces for each body pair should have normal vectors that are opposite.

To use the enumerated list, see [IEnumBodies2::Next](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumBodies2~Next.md), [IEnumBodies2::Skip](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumBodies2~Skip.md), [IEnumBodies2::Reset](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumBodies2~Reset.md), and [IEnumBodies2::Clone](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumBodies2~Clone.md).

If a component is suppressed or lightweight, this method might return NULL because the component has not been loaded into memory by SOLIDWORKS. For more information on lightweight components, see [Work With Lightweight Components](sldworksAPIProgGuide.chm::/OVERVIEW/Work_with_Lightweight_Components.htm).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)
