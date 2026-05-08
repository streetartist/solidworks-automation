# ReplaceComponents Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ReplaceComponents`

Obsolete. Superseded by IAssemblyDoc::ReplaceComponents2.
Obsolete. Superseded by [IAssemblyDoc::ReplaceComponents2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ReplaceComponents2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ReplaceComponents( _
   ByVal FileName As System.String, _
   ByVal ConfigName As System.String, _
   ByVal ReplaceAllInstance As System.Boolean, _
   ByVal ReAttachMates As System.Boolean _
) As System.Boolean
```

```

Dim instance As IAssemblyDoc
Dim FileName As System.String
Dim ConfigName As System.String
Dim ReplaceAllInstance As System.Boolean
Dim ReAttachMates As System.Boolean
Dim value As System.Boolean
 
value = instance.ReplaceComponents(FileName, ConfigName, ReplaceAllInstance, ReAttachMates)
```

```

System.bool ReplaceComponents( 
   System.string FileName,
   System.string ConfigName,
   System.bool ReplaceAllInstance,
   System.bool ReAttachMates
)
```

```

System.bool ReplaceComponents( 
   System.String^ FileName,
   System.String^ ConfigName,
   System.bool ReplaceAllInstance,
   System.bool ReAttachMates
) 
```

#### Parameters

*FileName*
:   Path and new file name

*ConfigName*
:   Name of configuration

*ReplaceAllInstance*
:   True to replace all instances, false to not

*ReAttachMates*
:   True to reattach all of the mates if the component is found in the subassembly component, false to not

#### Return Value

True if the component is successfully replaced, false if not

Remarks

You cannot replace a selected component with a component of the same name even if the components are in different folders.

The component must be a top-level component. It cannot be a component of a sub-assembly. If the application needs to replace a component of the sub-assembly, then it should open the sub-assembly and get the component from that assembly.

This method closes any component files when called in an assembly. If the components were modified, then those modifications are not automatically saved. You must save any modifications before closing the files.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::AddComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddComponents.md)  
[IAssemblyDoc::AddComponent5 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddComponent5.md)  
[IAssemblyDoc::IAddComponents2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IAddComponents2.md)  
[IModelDoc2::ReloadOrReplace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ReloadOrReplace.md)
