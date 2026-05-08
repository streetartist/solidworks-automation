# GetSystemTextureName Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture~GetSystemTextureName`

Gets the name of the texture that appears in the Texture PropertyManager.
Gets the name of the texture that appears in the Texture PropertyManager.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSystemTextureName( _
   ByVal FileNameIn As System.String, _
   ByRef Res As System.Boolean _
) As System.String
```

```

Dim instance As ITexture
Dim FileNameIn As System.String
Dim Res As System.Boolean
Dim value As System.String
 
value = instance.GetSystemTextureName(FileNameIn, Res)
```

```

System.string GetSystemTextureName( 
   System.string FileNameIn,
   out System.bool Res
)
```

```

System.String^ GetSystemTextureName( 
   System.String^ FileNameIn,
   [Out] System.bool Res
) 
```

#### Parameters

*FileNameIn*
:   Path and filename of texture (see **Remarks**)

*Res*
:   True if the name of the texture that appears in the Texture PropertyManager is returned, false if not

#### Return Value

Name of texture as it appears in the Texture PropertyManager (see Remarks)

Remarks

This method only supports SOLIDWORKS-supplied textures.

Call [ITexture::MaterialName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture~MaterialName.md) to get the value for FileNameIn before calling this method. ITexture::MaterialName returns an abbreviated path and the name of the texture as it appears in the Texture PropertyManager. For example, if ITexture::MaterialName returns *install\_dir***\data\images\textures\plastic\brushed\bred.jpg**, then this method returns Plastic\Brushed\Red.

Example

See the [ITexture](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITexture Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture.md)  
[ITexture Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture_members.md)
