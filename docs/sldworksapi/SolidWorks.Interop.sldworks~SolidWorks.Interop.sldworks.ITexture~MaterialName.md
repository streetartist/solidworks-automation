# MaterialName Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture~MaterialName`

Gets or sets the path and file name of the texture material.
Gets or sets the path and file name of the texture material.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property MaterialName As System.String
```

```

Dim instance As ITexture
Dim value As System.String
 
instance.MaterialName = value
 
value = instance.MaterialName
```

```

System.string MaterialName {get; set;}
```

```

property System.String^ MaterialName {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Path and file name of the texture (see **Remarks**)

Remarks

If the texture is a SOLIDWORKS-supplied texture, then the path returned is:

*install\_dir***\data\Images\textures\**texture\_library**\**texture\_type**\**texture\_image\_file

For example, *install\_dir*\data\Images\textures\plastic\brushed\bred.jpg.

If the texture is user-defined texture, then the path returned is:

     drive:**\***path\_name***\**texture\_image\_file

For example, D:\MyTextures\gear.jpg.

Call this property before calling [ITexture::GetSystemTextureName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture~GetSystemTextureName.md) to obtain a value for FileNameIn.

Example

See the [ITexture](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture.md) examples.

Example

[Remove Textures From Assembly Components (VBA)](Remove_Textures_from_Assembly_Components_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITexture Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture.md)  
[ITexture Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture_members.md)
