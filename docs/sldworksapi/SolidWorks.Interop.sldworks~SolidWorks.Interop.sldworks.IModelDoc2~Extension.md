# Extension Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Extension`

Gets the IModelDocExtension object, which also allows access to the model document.
Gets the [IModelDocExtension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md) object, which also allows access to the model document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property Extension As ModelDocExtension
```

```

Dim instance As IModelDoc2
Dim value As ModelDocExtension
 
value = instance.Extension
```

```

ModelDocExtension Extension {get;}
```

```

property ModelDocExtension^ Extension {
   ModelDocExtension^ get();
}
```

#### Property Value

[IModelDocExtension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md) object

Example

[Access Assembly (C++)](Access_Assembly_Example_CPlusPlus_COM.htm)  
[Create Cylinder (C++)](Create_Cylinder_Example_CPlusPlus_COM.htm)  
[Traverse Bodies (C++)](Traverse_Bodies_Example_CPlusPlusCLI.htm)  
[Get Names of Bodies in Multibody Part (VBA)](Get_Names_of_Bodies_in_MultiBody_Part_Example_VB.htm)  
[Insert Wrap Feature (VBA)](Insert_Wrap_Feature_Example_VB.htm)  
[Use Persistent Reference (VBA)](Use_Persistent_Reference_Example_VB.htm)  
[Create Equation-driven Curve (C#)](Create_Equation-driven_Curve_Example_CSharp.htm)  
[Create Equation-driven Curve (VB.NET)](Create_Equation-driven_Curve_Example_VBNET.htm)  
[Create Equation-driven Curve (VBA)](Create_Equation-driven_Curve_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
