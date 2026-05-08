# IAttributeDef Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef`

Allows access to an attribute definition.
Allows access to an attribute definition.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IAttributeDef 
```

```

Dim instance As IAttributeDef
```

```

public interface IAttributeDef 
```

```

public interface class IAttributeDef 
```

Remarks

An attribute definition is an application-specific data packet that is automatically saved with the SOLIDWORKS file and reloaded when the file is opened. An application can create [attribute](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute.md) data that is attached to an entity in a SOLIDWORKS document.

The attribute definition describes a template for the data packet. The definition contains the names of the parameters in the attribute, their types and default values. It also allows you to create instances of the definition on entities in your model.

The general sequence of steps in IAttribute creation is to:

1. Create an attribute definition ([ISldWorks::DefineAttribute](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~DefineAttribute.md))
2. Add parameters to the attribute definition ([IAttributeDef::AddParameter](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef~AddParameter.md))
3. Register the attribute definition ([IAttributeDef::Register](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef~Register.md))
4. Create instances of the attribute definition on objects throughout the model ([IAttributeDef::CreateInstance5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef~CreateInstance5.md))

Perform Steps 1 through 3 only once for each working session. In other words, perform Steps 1 through 3 when your DLL or EXE is initially loaded or run. Until the DLL is unloaded or the EXE is closed, you can create an unlimited number of instances of the attribute definition.

Example

[Create Attribute (VBA)](Create_Attribute_Example_VB.htm)  
[Add Attribute to Feature and Include in Library Feature (C#)](Add_Attribute_to_Feature_and_Include_in_Library_Feature_Example_CSharp.htm)  
[Add Attribute to Feature and Include in Library Feature (VB.NET)](Add_Attribute_to_Feature_and_Include_in_Library_Feature_Example_VBNET.htm)  
[Add Attribute to Feature and Include in Library Feature (VBA)](Add_Attribute_to_Feature_and_Include_In_Library_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAttributeDef Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
