# SavePackAndGo Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SavePackAndGo`

Saves the files designated for Pack and Go to either a folder or Zip file.
Saves the files designated for [Pack and Go](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo.md) to either a folder or Zip file.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SavePackAndGo( _
   ByVal PackAndGo As PackAndGo _
) As System.Object
```

```

Dim instance As IModelDocExtension
Dim PackAndGo As PackAndGo
Dim value As System.Object
 
value = instance.SavePackAndGo(PackAndGo)
```

```

System.object SavePackAndGo( 
   PackAndGo PackAndGo
)
```

```

System.Object^ SavePackAndGo( 
   PackAndGo^ PackAndGo
) 
```

#### Parameters

*PackAndGo*
:   [Pack and Go](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo.md) object

#### Return Value

Array of the status codes of Pack and Go as defined in [swPackAndGoSaveStatus\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPackAndGoSaveStatus_e.html)

Remarks

After providing Pack and Go input, call this method to execute Pack and Go and end the Pack and Go session. A subsequent call to this method will fail without again providing Pack and Go input.

Example

[Pack and Go an Assembly (C#)](Pack_and_Go_an_Assembly_Example_CSharp.htm)  
[Pack and Go an Assembly (VB.NET)](Pack_and_Go_an_Assembly_Example_VBNET.htm)  
[Pack and Go an Assembly (VBA)](Pack_and_Go_an_Assembly_Example_VB.htm)  
[Add and Remove Files from Pack and Go (C#)](Add_and_Remove_Files_from_Pack_and_Go_Example_CSharp.htm)  
[Add and Remove Files from Pack and Go (VB.NET)](Add_and_Remove_Files_from_Pack_and_Go_Example_VBNET.htm)  
[Add and Remove Files from Pack and Go (VBA)](Add_and_Remove_Files_from_Pack_and_Go_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)
