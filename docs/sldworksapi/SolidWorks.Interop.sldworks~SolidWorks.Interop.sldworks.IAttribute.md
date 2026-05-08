# IAttribute Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute`

Allows access to an attribute's values.
Allows access to an attribute's values.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IAttribute 
```

```

Dim instance As IAttribute
```

```

public interface IAttribute 
```

```

public interface class IAttribute 
```

Remarks

An attribute is a piece of information that can be stored on a [body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md), [component](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md), [entity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.md) ( [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md), [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md), [vertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md), [loop2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2.md), or [feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)), and [model](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md) if null.

After you place an attribute on an object, you can get the IAttribute object and get or set its parameter values. For example, you can place an attribute containing NC machining information on a face. You can then use that attribute in automation on the shop floor to know what feed or speed to use during the machining process.

You can also add attributes to a [document object](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md).

From the attribute instance you can get the:

- Attribute definition
- Associated entity
- Parameter values
- Instance name

Example

[Add Attribute to Feature and Include in Library Feature (C#)](Add_Attribute_to_Feature_and_Include_in_Library_Feature_Example_CSharp.htm)  
[Add Attribute to Feature and Include in Library Feature (VB.NET)](Add_Attribute_to_Feature_and_Include_in_Library_Feature_Example_VBNET.htm)  
[Add Attribute to Feature and Include in Library Feature (VBA)](Add_Attribute_to_Feature_and_Include_In_Library_Feature_Example_VB.htm)  
[Delete Attribute (C#)](Delete_Attribute_Example_CSharp.htm)  
[Delete Attribute (VB.NET)](Delete_Attribute_Example_VBNET.htm)  
[Delete Attribute (VBA)](Delete_Attribute_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAttribute Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
