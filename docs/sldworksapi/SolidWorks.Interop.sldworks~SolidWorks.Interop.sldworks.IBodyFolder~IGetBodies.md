# IGetBodies Method (IBodyFolder)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~IGetBodies`

Gets the bodies in the folder.
Gets the bodies in the folder.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetBodies( _
   ByVal Count As System.Integer _
) As Body2
```

```

Dim instance As IBodyFolder
Dim Count As System.Integer
Dim value As Body2
 
value = instance.IGetBodies(Count)
```

```

Body2 IGetBodies( 
   System.int Count
)
```

```

Body2^ IGetBodies( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of bodies in the folder

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [IBody2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) objects

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

This method gets the bodies in the folder; it does not get the bodies in any subfolders. See [Accessing Bodies in Body Folders](sldworksAPIProgGuide.chm::/OVERVIEW/Accessing_Bodies_in_Body_Folders.htm) for details about the BodyFolder interface.

To get the number of bodies in the folder, use [IBodyFolder::GetBodyCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~GetBodyCount.md) before using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBodyFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder.md)  
[IBodyFolder Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder_members.md)  
[IBodyFolder::GetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~GetBodies.md)
