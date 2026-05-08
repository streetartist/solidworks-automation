# Type Property (IBodyFolder)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~Type`

Gets the type of body folder.
Gets the type of body folder.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property Type As System.Integer
```

```

Dim instance As IBodyFolder
Dim value As System.Integer
 
value = instance.Type
```

```

System.int Type {get;}
```

```

property System.int Type {
   System.int get();
}
```

#### Property Value

Type of body folder as defined in [swBodyFolderFeatureType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBodyFolderFeatureType_e.html)

Remarks

See [Accessing Bodies in Body Folders](sldworksAPIProgGuide.chm::/OVERVIEW/Accessing_Bodies_in_Body_Folders.htm) for details about the BodyFolder interface.

Example

[Get Bodies in Body Folders (VBA)](Get_Bodies_in_Body_Folders_Example_VB.htm)  
[Get SolidBodies from Cut-list Folders and Get Custom Properties (VBA)](Get_Solid_Bodies_from_Cut-list_Folders_and_Get_Custom_Properties_Example_VB.htm)  
[Get Bodies in Body Folders (VB.NET)](Get_Bodies_in_Body_Folders_Example_VBNET.htm)  
[Get Bodies in Body Folders (C#)](Get_Bodies_in_Body_Folders_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBodyFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder.md)  
[IBodyFolder Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder_members.md)
