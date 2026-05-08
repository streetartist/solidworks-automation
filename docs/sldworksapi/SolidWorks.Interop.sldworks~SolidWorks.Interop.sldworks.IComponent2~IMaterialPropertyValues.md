# IMaterialPropertyValues Property (IComponent2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IMaterialPropertyValues`

Gets or sets the material properties for the selected component in the active configuration.
Gets or sets the material properties for the selected component in the active configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property IMaterialPropertyValues As System.Double
```

```

Dim instance As IComponent2
Dim value As System.Double
 
instance.IMaterialPropertyValues = value
 
value = instance.IMaterialPropertyValues
```

```

System.double IMaterialPropertyValues {get; set;}
```

```

property System.double IMaterialPropertyValues {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Array of doubles describing the material's values on this component (see **Remarks**)

Remarks

The material values include the component color (R,G,B values), reflectivity (ambient, diffuse, specular, shininess), transparency, and emission. Valid values are from 0 to 1 for all values.

The format of the parameters or return values is an array of doubles as follows:

**[** *R, G, B, Ambient, Diffuse, Specular, Shininess, Transparency, Emission* **]**

To see a color change, you must:

1. Specify *R*, *G*, and *B*, each with a value between 0.0 and 1.0, inclusive. (These values are internally multiplied by 255.0 to determine the RGB color.)
2. Specify the reflectivity properties (*Diffuse*, *Specular*, *Shininess* (1.0 - Specular spread/Blurriness)), each with a value greater than 0.0 and less than or equal to 1.0.
3. Specify *Ambient*, *Transparency* and *Emission*, each with a value between 0.0 and 1.0, inclusive.
4. Refresh the graphics area after setting this property.

This method returns an S\_false HRESULT for COM implementations if the user has not explicitly modified this component from the material property values of the underlying part document. For example, the user can right-click a component in the FeatureManager design tree and select **Component Properties** to change the color. If the user has not done this, then this method returns NULL color information.

The default component color can be obtained from the component's [IModelDoc2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md) object ([IComponent2::IGetModelDoc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetModelDoc.md)) using IModelDoc2::MaterialPropertyValues.

You might also want to check for specific face colors using [IFace2::IMaterialPropertyValues](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IMaterialPropertyValues.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IComponent2::MaterialPropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~MaterialPropertyValues.md)  
[IComponent2::GetMaterialPropertyValues2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetMaterialPropertyValues2.md)  
[IComponent2::IGetMaterialPropertyValues2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetMaterialPropertyValues2.md)  
[IComponent2::IRemoveMaterialProperty2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IRemoveMaterialProperty2.md)  
[IComponent2::RemoveMaterialProperty2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~RemoveMaterialProperty2.md)  
[IComponent2::ISetMaterialPropertyValues2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~ISetMaterialPropertyValues2.md)  
[IComponent2::SetMaterialPropertyValues2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetMaterialPropertyValues2.md)
